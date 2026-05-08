from models.animation_state import AnimationState


class BubbleSort:

    @staticmethod
    def sort(data):

        arr = data.copy()

        n = len(arr)

        sorted_indices = []

        for i in range(n):

            for j in range(0, n - i - 1):

                yield AnimationState(
                    arr.copy(),
                    active_indices=[j, j + 1],
                    sorted_indices=sorted_indices.copy()
                )

                if arr[j] > arr[j + 1]:

                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

                    yield AnimationState(
                        arr.copy(),
                        active_indices=[j, j + 1],
                        sorted_indices=sorted_indices.copy()
                    )

            sorted_indices.append(n - i - 1)

        yield AnimationState(
            arr.copy(),
            sorted_indices=list(range(n))
        )