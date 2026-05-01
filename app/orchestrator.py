from agents.extract_agent import extract_agent
from agents.risk_agent import risk_agent
from agents.summary_agent import summary_agent
from tools.search_tool import mock_search

def run_pipeline(text):
    data = extract_agent(text)

    # tool usage
    insights = []
    for s in data.get("symptoms", []):
        insights.append(mock_search(s))

    risk = risk_agent(str(data))

    summary = summary_agent(data, risk)

    return {
        "structured_data": data,
        "tool_insights": insights,
        "risk": risk,
        "summary": summary
    }
