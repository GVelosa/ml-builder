
class MLProject:
    def __init__(self):
        self.name = None
        self.dataframe = None
        self.target = None
        self.features = None
        self.column_types = {}
        self.problem_type = None
        self.preprocessing_config = {}
        self.selected_models = []
        self.trained_models = {}
        self.results = {}
        self.completed_steps = set()