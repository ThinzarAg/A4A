from google.adk.tools.function_tool import FunctionTool


def create_study_plan(goal: str, period: str, current_status: str) -> str:
    """Creates daily study schedules and long-term skill development plans for university students.

    Args:
        goal: The goal to achieve (e.g., TOEIC 800 points, Python web app development)
        period: The timeframe to achieve the goal (e.g., 3 months from now, until graduation)
        current_status: Current study situation or available study time (e.g., can study 10 hours a week, beginner in programming)

    Returns:
        A study plan in Markdown format.
    """
    plan_output = f"# Study Plan\n\n"

    # Long-term Skill Development Plan
    plan_output += f"## Long-term Skill Development Plan\n\n"
    plan_output += f"### Goal: {goal}\n"
    plan_output += f"### Period: {period}\n\n"

    # This generates a provisional long-term plan. More detailed logic is needed based on period and goal.
    plan_output += f"| Phase | Duration | Objective |\n"
    plan_output += f"|---|---|---|\n"
    plan_output += f"| Phase 1 | Initial Stage | Understand the basics of {goal.split(" ")[0]} |\n" # Uses the first word of the goal as an example
    plan_output += f"| Phase 2 | Mid-term | Practically apply {goal.split(" ")[0]} |\n"
    plan_output += f"| Phase 3 | Final Stage | Apply {goal.split(" ")[0]} and complete a project |\n\n"

    # Daily Study Plan
    plan_output += f"## Daily Study Plan\n\n"
    plan_output += f"### This Week's Goal: Study to achieve Phase 1 objectives\n\n" # Linked to long-term plan
    
    # This generates a provisional daily plan. More detailed logic is needed based on goal, period, and current status.
    plan_output += f"| Day | Time | Content |\n"
    plan_output += f"|---|---|---|\n"
    plan_output += f"| Mon | 1-2 hours | Read basic books on {goal.split(" ")[0]}, watch online courses |\n"
    plan_output += f"| Tue | 1-2 hours | Summarize basic concepts of {goal.split(" ")[0]} in notes, solve practice problems |\n"
    plan_output += f"| Wed | 1-2 hours | Review Tuesday's content, search for related information online, check progress |\n"
    plan_output += f"| Thu | 1-2 hours | Create a simple program using the basics of {goal.split(" ")[0]} (if applicable) |\n"
    plan_output += f"| Fri | 1-2 hours | Review the week's learning, adjust next week's plan |\n"
    plan_output += f"| Sat | 2-3 hours | Intensive study or deep dive into interesting related topics |\n"
    plan_output += f"| Sun | Rest/Free Study | Rest or light review, activities to maintain motivation |\n\n"

    plan_output += f"* The above is a suggestion only. Please adjust it to your own pace, considering your current status: {current_status}.\n"
    plan_output += f"Flexibly changing the plan according to your progress and continuing without overexertion is key to success."

    return plan_output


# FunctionToolとして登録
create_study_plan_tool = FunctionTool(func=create_study_plan)
