import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """ scrape information from linkedin profile,
     Manually scrape information from linkedin profile"""
    
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/Isabelle16/a82502c623c6a82de4b6d4698aa4d66b/raw/71f6d2957b2291c316720fb7a43bc8009400dbc6/isa_profile.JSON"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    
    else:
        header_dic = {'Authorization': f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        response = requests.get(
            api_endpoint,
            params={'url': linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )
    
    data = response.json()


    # remove empty fields and unwanted fields - keep only relevant tokens!
    data = {
        k: v 
        for k, v in data.items() 
        if v not in ([], "", " ", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
        
    return data
    

if __name__ == "__main__":
    
    linkedin_profile_url = "https://www.linkedin.com/in/masieroisabella/"
    print(scrape_linkedin_profile(linkedin_profile_url, True))