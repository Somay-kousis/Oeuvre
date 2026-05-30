
# Self.so
```

  a portfolio with opinions.
```

---

your portfolio doesn't talk.
it just sits there being a website.

this one talks back.

`self.so` is a RAG system built on top of a person's actual memory —
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
project       project           casper, mutiny — the real bets
archive       query_only        old projects, early experiments
```

the system knows the difference between something that *defines you*
and something you shipped two years ago.

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

two context streams run separately —
`factual_context` for what to say,
`style_context` for how it should feel.

the model reads the room.
recruiter question → grounded and useful.
casual message → casual back.
someone types "lmao true" → continues the thought, doesn't reset.

---

## structure

```
self.so/
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
git clone https://github.com/yourusername/self.so
cd self.so

cp .env.example .env
# fill: GROQ_API_KEY · SUPABASE_URL · SUPABASE_ANON_KEY · JINA_API_KEY

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

## stack

```
backend     fastapi + uvicorn
llm         groq  ·  llama-3.1-8b-instant
embeddings  jina-embeddings-v3
vectors     supabase + pgvector
framework   langchain
runtime     python 3.11
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

---

```
built by somay
the kind of project that only makes sense if you've thought
too hard about how to represent yourself on the internet.
```
