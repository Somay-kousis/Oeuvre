
# Oeuvre

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11.9-3776AB.svg" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-backend-009688.svg" alt="FastAPI" />
  <img src="https://img.shields.io/badge/LangChain-RAG-1C3C3C.svg" alt="LangChain" />
  <img src="https://img.shields.io/badge/Groq-LLM-F55036.svg" alt="Groq" />
  <img src="https://img.shields.io/badge/Jina-embeddings-009191.svg" alt="Jina" />
  <img src="https://img.shields.io/badge/Supabase-vector%20store-3FCF8E.svg" alt="Supabase" />
</p>

```

  a portfolio with opinions.
```

---

your portfolio doesn't talk.
it just sits there being a website.

this one talks back.

`Oeuvre` is a RAG system built on top of a person's actual memory:
writing, taste, projects, values, contradictions, what they're building,
what they believe, who they are.

ask it something. it finds the right pieces. answers like a person would.

---

```
                     ┌─────────────────────────────────────────┐
                     │           the memory                    │
                     │                                         │
                     │   identity · values · tone · projects   │
                     │   writing · relationships · ambitions   │
                     │   current work · career · philosophy    │
                     │                                         │
                     │         (your markdown files)           │
                     └──────────────────┬──────────────────────┘
                                        │
                                        ▼
                     ┌─────────────────────────────────────────┐
                     │           jina embeddings               │
                     │      dense vectors of who you are       │
                     └──────────────────┬──────────────────────┘
                                        │
                                        ▼
                     ┌─────────────────────────────────────────┐
                     │         supabase pgvector               │
                     │       stored, queryable, fast           │
                     └──────────────────┬──────────────────────┘
                                        │
                           ┌────────────┴────────────┐
                           ▼                         ▼
               ┌───────────────────┐     ┌───────────────────┐
               │  factual context  │     │   style context   │
               │  (what to say)    │     │  (how to say it)  │
               └────────┬──────────┘     └─────────┬─────────┘
                        │                          │
                        └────────────┬─────────────┘
                                     ▼
                     ┌─────────────────────────────────────────┐
                     │        groq / llama-3.1-8b              │
                     │                                         │
                     │   responds like a person, not a bot     │
                     └─────────────────────────────────────────┘
```

---

## memory isn't flat

every file knows what it is.

```
memory_type   retrieval_mode    what lives here
──────────────────────────────────────────────────────────
core          always            identity, values, tone, presence
core          emotional         mind, relationships, vision of love
core          writing           writings, aesthetics, creativity
dynamic       recent            current work, resume, career strategy
dynamic       learning          gen ai journey, learning roadmap
project       project           casper, rabbithole, something (the real bets)
archive       query_only        old projects, early experiments
```

the tags tell apart something that *defines you*
and something you shipped two years ago.

honest note: retrieval doesn't read them yet.
right now it's plain top-5 similarity, plus 3 style chunks.
the tags are there for when it does.

---

## the prompt is the product

most portfolio bots fail in the same two ways:

```
failure mode A: corporate bot
> "Great question! Somay has experience in..."

failure mode B: try-hard bot  
> "omg yes!!! he's SO passionate about..."
```

the system prompt here draws a hard line:

> *you are not a generic assistant.
> you are not fully Somay either.
> you are a conversational narrator.*

two context streams run separately.
`factual_context` for what to say,
`style_context` for how it should feel.

the model reads the room.
recruiter question → grounded and useful.
casual message → casual back.
someone types "lmao true" → continues the thought, doesn't reset.

---

## structure

```
Oeuvre/
│
├── app/
│   ├── main.py           ← fastapi entry
│   ├── chat.py           ← the brain: retrieval + merge + generate
│   ├── prompts.py        ← the soul: what kind of thing this is
│   ├── vectorstore.py    ← supabase pgvector
│   ├── embeddings.py     ← jina-embeddings-v3
│   ├── ingest.py         ← memory → vectors
│   ├── loader.py         ← markdown → chunks
│   └── config.py         ← env + constants
│
├── data/                 ← your memory (gitignored, obviously)
├── add_metadata.py       ← stamps frontmatter onto memory files
├── requirements.txt
└── .env.example
```

---

## run it

```bash
git clone https://github.com/Somay-kousis/Oeuvre
cd Oeuvre

cp .env.example .env
# fill: GROQ_API_KEY · SUPABASE_URL · SUPABASE_SERVICE_KEY · JINA_API_KEY

pip install -r requirements.txt

python add_metadata.py          # stamp your memory files
python -m app.ingest            # push to vector store
uvicorn app.main:app --reload   # start server
```

then:

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "what is he building right now?"}'
```

---

## fork it for yourself

the architecture is general. the memory is personal.

```
1. replace /data/*.md with your own writing
2. update metadata_map in add_metadata.py
3. rewrite the system prompt in prompts.py to match your voice
4. ingest → run → point a frontend at /ask
```

the rest is yours.

one catch: the conversation summary is a single global.
everyone talking to the server shares one memory of the chat.
fine for a demo, not for real traffic.

---

```
built by somay
the kind of project that only makes sense if you've thought
too hard about how to represent yourself on the internet.
```
