class AnimationState:
    def __init__(self, data, active_indices=None, sorted_indices=None):
        self.data = data
        self.active_indices = active_indices or []
        self.sorted_indices = sorted_indices or []