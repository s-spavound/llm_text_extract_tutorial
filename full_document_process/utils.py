import re
import tiktoken

enc = tiktoken.get_encoding("gpt-4")

def chunk_on_colon_boundary(text: str, max_tokens: int = 10000) -> list[str]:
    tokens = enc.encode(text)
    chunks = []
    start = 0
    L = len(tokens)

    while start < L:
        end = min(start + max_tokens, L)
        chunk = enc.decode(tokens[start:end])
        remaining = enc.decode(tokens[end:])
        match = re.search(
            r"(?:^|\n)(?:Dr|Mr|Mrs|Ms|Prof|Chair|Lt)\.?\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*:",
            remaining,
            re.IGNORECASE,
        )
        if match:
            colon_idx = match.start()
            extra = remaining[:colon_idx]
            combined = chunk + extra
            end = start + len(enc.encode(combined))
        else:
            combined = chunk
        chunks.append(combined)
        start = end

    return chunks