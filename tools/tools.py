from langchain_community.tools.tavily_search import TavilySearchResults

# Tavily: search API optimised for generative-AI applications (e.g. RAG)


def get_profile_url_tavily(name: str) -> str:
    """Get the LinkedIn profile URL of a person using Tavily's search API"""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res[0]["url"]  # parse the Tavily response


if __name__ == "__main__":
    print(get_profile_url_tavily(name="Isabella Masiero"))
