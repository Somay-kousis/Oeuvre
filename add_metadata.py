from pathlib import Path

DATA_DIR = Path("data")

metadata_map = {
    "tone": {"category": "voice", "priority": 10, "memory_type": "core", "retrieval_mode": "always", "volatility": "stable"},
    "presence": {"category": "emotional_identity", "priority": 10, "memory_type": "core", "retrieval_mode": "always", "volatility": "stable"},
    "me": {"category": "identity", "priority": 10, "memory_type": "core", "retrieval_mode": "always", "volatility": "stable"},
    "futureme": {"category": "future_identity", "priority": 10, "memory_type": "core", "retrieval_mode": "always", "volatility": "stable"},
    "themes": {"category": "identity", "priority": 10, "memory_type": "core", "retrieval_mode": "always", "volatility": "stable"},
    "skillsandcraft": {"category": "skills", "priority": 10, "memory_type": "core", "retrieval_mode": "always", "volatility": "medium"},
    "relationships": {"category": "relationships", "priority": 10, "memory_type": "core", "retrieval_mode": "emotional", "volatility": "stable"},

    "writings": {"category": "writing_voice", "priority": 10, "memory_type": "core", "retrieval_mode": "writing", "volatility": "stable"},
    "aesthetics": {"category": "aesthetic_identity", "priority": 9, "memory_type": "core", "retrieval_mode": "design", "volatility": "stable"},
    "creativity": {"category": "creative_identity", "priority": 9, "memory_type": "core", "retrieval_mode": "writing", "volatility": "stable"},
    "story": {"category": "personal_story", "priority": 8, "memory_type": "core", "retrieval_mode": "reflection", "volatility": "stable"},

    "mind": {"category": "psychology", "priority": 9, "memory_type": "core", "retrieval_mode": "emotional", "volatility": "stable"},
    "principles": {"category": "values", "priority": 10, "memory_type": "core", "retrieval_mode": "always", "volatility": "stable"},
    "values": {"category": "values", "priority": 9, "memory_type": "core", "retrieval_mode": "always", "volatility": "stable"},
    "philosophy": {"category": "philosophy", "priority": 9, "memory_type": "core", "retrieval_mode": "reflection", "volatility": "stable"},
    "visionoflove": {"category": "relationships", "priority": 8, "memory_type": "core", "retrieval_mode": "emotional", "volatility": "stable"},
    "life_systems": {"category": "systems", "priority": 8, "memory_type": "core", "retrieval_mode": "planning", "volatility": "medium"},
    "impactandservice": {"category": "values", "priority": 8, "memory_type": "core", "retrieval_mode": "career", "volatility": "stable"},

    "workandambition": {"category": "ambition", "priority": 9, "memory_type": "core", "retrieval_mode": "career", "volatility": "stable"},
    "currentworks": {"category": "current_context", "priority": 10, "memory_type": "dynamic", "retrieval_mode": "recent", "volatility": "high"},
    "resume": {"category": "career", "priority": 9, "memory_type": "dynamic", "retrieval_mode": "career", "volatility": "high"},
    "internshipstrategy": {"category": "career", "priority": 9, "memory_type": "dynamic", "retrieval_mode": "career", "volatility": "medium"},
    "learningroadmap": {"category": "learning", "priority": 9, "memory_type": "dynamic", "retrieval_mode": "learning", "volatility": "medium"},
    "genaijourney": {"category": "learning", "priority": 9, "memory_type": "dynamic", "retrieval_mode": "learning", "volatility": "medium"},
    "technicalnotes": {"category": "technical_thinking", "priority": 7, "memory_type": "dynamic", "retrieval_mode": "technical", "volatility": "medium"},

    "cofoundermemory": {"category": "flagship_project", "priority": 10, "memory_type": "project", "retrieval_mode": "project", "volatility": "high"},
    "something": {"category": "vision_project", "priority": 10, "memory_type": "project", "retrieval_mode": "project", "volatility": "medium"},
    "rabbithole": {"category": "flagship_project", "priority": 9, "memory_type": "project", "retrieval_mode": "project", "volatility": "high"},
    "thelastlibrary": {"category": "flagship_project", "priority": 9, "memory_type": "project", "retrieval_mode": "project", "volatility": "high"},
    "casper": {"category": "vision_project", "priority": 9, "memory_type": "project", "retrieval_mode": "project", "volatility": "medium"},
    "steelcareer": {"category": "major_project", "priority": 7, "memory_type": "project", "retrieval_mode": "query_only", "volatility": "low"},
    "zuuush": {"category": "small_project", "priority": 3, "memory_type": "archive", "retrieval_mode": "query_only", "volatility": "low"},
    "customerchurn": {"category": "small_project", "priority": 3, "memory_type": "archive", "retrieval_mode": "query_only", "volatility": "low"},
    "houseprice": {"category": "small_project", "priority": 3, "memory_type": "archive", "retrieval_mode": "query_only", "volatility": "low"},
    "muggleproof": {"category": "early_project", "priority": 3, "memory_type": "archive", "retrieval_mode": "query_only", "volatility": "low"},
    "portfoliowebsite": {"category": "portfolio_project", "priority": 5, "memory_type": "archive", "retrieval_mode": "query_only", "volatility": "low"},

    "github": {"category": "social_profile", "priority": 7, "memory_type": "dynamic", "retrieval_mode": "profile", "volatility": "medium"},
    "links": {"category": "reference", "priority": 6, "memory_type": "dynamic", "retrieval_mode": "profile", "volatility": "medium"},
    "wins": {"category": "achievements", "priority": 8, "memory_type": "core", "retrieval_mode": "confidence", "volatility": "medium"},
    "hackathons": {"category": "opportunities", "priority": 7, "memory_type": "dynamic", "retrieval_mode": "career", "volatility": "high"},
}

def has_frontmatter(text):
    return text.startswith("---\n")

for md_file in DATA_DIR.glob("*.md"):
    name = md_file.stem
    text = md_file.read_text(encoding="utf-8")

    if has_frontmatter(text):
        print(f"Skipped existing metadata: {md_file}")
        continue

    meta = metadata_map.get(name, {
        "category": "general",
        "priority": 5,
        "memory_type": "general",
        "retrieval_mode": "query_only",
        "volatility": "medium",
    })

    frontmatter_lines = ["---"]
    frontmatter_lines.append(f"title: {name}")

    for key, value in meta.items():
        frontmatter_lines.append(f"{key}: {value}")

    frontmatter_lines.append("source_type: markdown_memory")
    frontmatter_lines.append("---")
    frontmatter_lines.append("")

    frontmatter = "\n".join(frontmatter_lines) + "\n"

    md_file.write_text(frontmatter + text, encoding="utf-8")
    print(f"Added metadata: {md_file}")