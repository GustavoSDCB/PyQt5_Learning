class Notebook:
    def __init__(self, asset_id: int, lab: int, state: str):
        self.asset_id = asset_id
        self.lab = lab
        self.state = state

    def to_dict(self) -> dict[str, object]:
        return {
            'asset_id' : self.asset_id,
            'lab': self.lab,
            'state': self.state
        }

LABEL = {
    'asset_id': 'Asset ID',
    'lab': 'Movable Lab',
    'state': 'State'
}

if __name__ == "__main__":
    note = Notebook(42864, 4, "Working")
 
    for key, value in note.to_dict().items():
        formatted_line = f"{LABEL.get(key, key)}: {value}"
        print(formatted_line, end=' | ')
    