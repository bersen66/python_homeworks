
class Matrix:

    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._matrix = [[0 for _ in range(self._cols)] for _ in range(rows)]

    @classmethod
    def from_numpy(cls, np_array):
        rows, cols = np_array.shape
        instance = cls(rows, cols)
        instance._matrix = np_array.tolist()
        return instance

    def __getitem__(self, index):
        return self._matrix[index]

    def __setitem__(self, index, value):
        self._matrix[index] = value

    def __str__(self):
        '''Возвращает строковое представление матрицы'''
        # Делаем вывод с выравниванием
        max_width = max(len(str(item)) for row in self._matrix for item in row) + 2  # Ширина для выравнивания
        rows_str = []
        for row in self._matrix:
            row_str = "[" + ", ".join(f"{item:>{max_width}}" for item in row) + "]"  # Выравнивание по правому краю
            rows_str.append(row_str)
        return "\n".join(rows_str)

    def _throw_if_mismatched_dimensions(self, other, compare="exact"):
        if compare == "exact":
            if (self._rows, self._cols) != (other._rows, other._cols):
                raise ValueError("Mismatched dimensions!")
        elif compare == "multiply":
            if self._cols != other._rows:
                raise ValueError("lhs rows num must be equal to rhs cols num")

    def __mul__(self, other):
        '''Покомпонентное умножение'''
        self._throw_if_mismatched_dimensions(other, "exact")
        return self._component_job(other, lambda x, y: x * y)

    def __add__(self, other):
        '''Сложение матриц'''
        self._throw_if_mismatched_dimensions(other, "exact")
        return self._component_job(other, lambda x, y: x + y)

    def __matmul__(self, rhs):
        '''Математическое перемножение'''
        self._throw_if_mismatched_dimensions(rhs, "multiply")
        return self._math_multiply(rhs)

    def _component_job(self, other, job):
        result = Matrix(self._rows, self._cols)
        for i in range(self._rows):
            for j in range(self._cols):
                result[i][j] = job(self._matrix[i][j], other[i][j])
        return result

    def _math_multiply(self, other):
        result = Matrix(self._rows, other._cols)

        for i in range(self._rows):
            for j in range(other._cols):
                for k in range(self._cols):
                    result._matrix[i][j] += self._matrix[i][k] * other._matrix[k][j]

        return result
