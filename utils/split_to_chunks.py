from typing import Any

# разделение указанного массива на части указанного размера
def split_to_chunks(arr: list[Any], chunk_size: int) -> list[list[Any]]:
    chunks: list[list[Any]] = []

    chunk_size = 2

    for i in range(0, len(arr) - 1, chunk_size):
        chunks.append(arr[i:i + chunk_size])

    return chunks
