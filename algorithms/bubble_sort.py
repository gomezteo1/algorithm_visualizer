from models.animation_state import AnimationState


class BubbleSort:

    @staticmethod
    def sort(data):

        arr = data.copy()

        n = len(arr)

        sorted_indices = []

        comparisons = 0

        swaps = 0

        for i in range(n):

            for j in range(0, n - i - 1):

                comparisons += 1

                yield AnimationState(
                    data=arr.copy(),
                    active_indices=[j, j + 1],
                    sorted_indices=sorted_indices.copy(),
                    message=(
                        f"Comparando {arr[j]} y {arr[j + 1]}"
                    ),
                    comparisons=comparisons,
                    swaps=swaps
                )

                if arr[j] > arr[j + 1]:

                    arr[j], arr[j + 1] = (
                        arr[j + 1],
                        arr[j]
                    )

                    swaps += 1

                    yield AnimationState(
                        data=arr.copy(),
                        active_indices=[j, j + 1],
                        sorted_indices=sorted_indices.copy(),
                        message=(
                            f"{arr[j]} y {arr[j + 1]} "
                            f"fueron intercambiados"
                        ),
                        comparisons=comparisons,
                        swaps=swaps
                    )

            sorted_indices.append(n - i - 1)

        yield AnimationState(
            data=arr.copy(),
            sorted_indices=list(range(n)),
            message="Array completamente ordenado",
            comparisons=comparisons,
            swaps=swaps
        )