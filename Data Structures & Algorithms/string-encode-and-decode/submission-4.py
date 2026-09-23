class Solution:
    # keep track of some sort of spacing rule?
    def encode(self, strs: List[str]) -> str:
        self.strings = strs
        return ''.join(strs)

    def decode(self, s: str) -> List[str]:
        return self.strings
