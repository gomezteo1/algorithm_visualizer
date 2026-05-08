class AnimationState:

    def __init__(
        self,
        data,
        active_indices=None,
        sorted_indices=None,
        message="",
        comparisons=0,
        swaps=0
    ):

        self.data = data

        self.active_indices = active_indices or []

        self.sorted_indices = sorted_indices or []

        self.message = message

        self.comparisons = comparisons

        self.swaps = swaps