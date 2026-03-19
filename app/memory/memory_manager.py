# filename: app/memory/memory_manager.py

from typing import Dict, List


class SimpleMemory:
    def __init__(self):
        self.store: Dict[str, List[dict]] = {}

    def get_messages(self, thread_id: str) -> List[dict]:
        return self.store.get(thread_id, []).copy()

    def add_user_message(self, thread_id: str, content: str) -> None:
        self.store.setdefault(thread_id, []).append(
            {"role": "user", "content": content}
        )

    def add_assistant_message(self, thread_id: str, content: str) -> None:
        self.store.setdefault(thread_id, []).append(
            {"role": "assistant", "content": content}
        )

    def clear(self, thread_id: str) -> None:
        self.store.pop(thread_id, None)


memory = SimpleMemory()