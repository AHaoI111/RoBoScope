from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QPainter, QPen, QColor, QBrush, Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton


class ScanWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_rows = 1  # 网格行数
        self.grid_cols = 1  # 网格列数
        self.grid_colors = []  # 存储每个网格的颜色状态
        self.update_grid_colors()  # 初始化颜色状态

    def set_grid_size(self, rows, cols):
        """设置网格数量"""
        self.grid_rows = rows
        self.grid_cols = cols
        self.update_grid_colors()  # 更新颜色状态
        self.update()  # 触发重绘

    def update_grid_colors(self):
        """初始化或更新网格颜色状态"""
        # 将所有网格的颜色初始化为透明（未填充）
        self.grid_colors = [
            [QColor(0, 0, 0, 0) for _ in range(self.grid_cols)] for _ in range(self.grid_rows)
        ]

    def fill_grid(self, row, col, color):
        """
        填充指定网格的颜色。

        参数:
        row: 网格的行索引（从 0 开始）。
        col: 网格的列索引（从 0 开始）。
        color: QColor 对象，表示要填充的颜色。
        """
        if 0 <= row < self.grid_rows and 0 <= col < self.grid_cols:
            self.grid_colors[row][col] = color
            self.update()  # 触发重绘

    def clear_grid(self):
        """清空所有网格的颜色"""
        self.update_grid_colors()  # 重置颜色状态
        self.update()  # 触发重绘

    def clear_all(self):
        """清空网格（移除网格线和颜色）"""
        self.grid_rows = 0  # 设置行数为 0
        self.grid_cols = 0  # 设置列数为 0
        self.grid_colors = []  # 清空颜色状态
        self.update()  # 触发重绘

    def paintEvent(self, event):
        """重写绘制事件"""
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 如果网格行数和列数为 0，则不绘制网格
        if self.grid_rows == 0 or self.grid_cols == 0:
            return

        # 计算每个网格的宽度和高度
        grid_width = self.width() / self.grid_cols
        grid_height = self.height() / self.grid_rows

        # 绘制网格和填充颜色
        for row in range(self.grid_rows):
            for col in range(self.grid_cols):
                rect = QRect(
                    int(col * grid_width),
                    int(row * grid_height),
                    int(grid_width),
                    int(grid_height),
                )

                # 填充网格颜色
                color = self.grid_colors[row][col]
                if color.alpha() > 0:  # 如果颜色不透明
                    painter.fillRect(rect, QBrush(color))

                # 绘制网格线
                pen = QPen(Qt.gray, 1, Qt.SolidLine)
                painter.setPen(pen)
                painter.drawRect(rect)


