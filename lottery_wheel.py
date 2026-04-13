import tkinter as tk
import random
import math

class LotteryWheel:
    def __init__(self, root):
        self.root = root
        self.root.title("抽籤系統 - 1-22號轉盤")
        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()

        self.numbers = list(range(1, 23))  # 1 to 22
        self.num_sections = len(self.numbers)
        self.angle_per_section = 360 / self.num_sections
        self.current_angle = 0
        self.spinning = False
        self.spin_speed = 0

        self.draw_wheel()

        self.spin_button = tk.Button(root, text="旋轉", command=self.spin)
        self.spin_button.pack()

        self.result_label = tk.Label(root, text="", font=("Arial", 16))
        self.result_label.pack()

    def draw_wheel(self):
        self.canvas.delete("all")
        center_x, center_y = 200, 200
        radius = 150

        for i, num in enumerate(self.numbers):
            start_angle = i * self.angle_per_section + self.current_angle
            end_angle = (i + 1) * self.angle_per_section + self.current_angle

            # Draw section
            color = "lightblue" if i % 2 == 0 else "lightgreen"
            self.canvas.create_arc(center_x - radius, center_y - radius,
                                   center_x + radius, center_y + radius,
                                   start=start_angle, extent=self.angle_per_section,
                                   fill=color, outline="black")

            # Draw number
            mid_angle = math.radians(start_angle + self.angle_per_section / 2)
            text_x = center_x + (radius - 30) * math.cos(mid_angle)
            text_y = center_y + (radius - 30) * math.sin(mid_angle)
            self.canvas.create_text(text_x, text_y, text=str(num), font=("Arial", 12, "bold"))

        # Draw pointer
        pointer_x = center_x
        pointer_y = center_y - radius - 20
        self.canvas.create_polygon(pointer_x, pointer_y, pointer_x - 10, pointer_y + 20,
                                   pointer_x + 10, pointer_y + 20, fill="red")

    def spin(self):
        if self.spinning:
            return
        self.spinning = True
        self.spin_speed = random.randint(10, 20)  # Initial speed
        self.animate_spin()

    def animate_spin(self):
        if self.spin_speed > 0:
            self.current_angle += self.spin_speed
            self.current_angle %= 360
            self.draw_wheel()
            self.spin_speed -= 0.5  # Decelerate
            self.root.after(50, self.animate_spin)
        else:
            self.spinning = False
            self.show_result()

    def show_result(self):
        # Calculate which section the pointer is pointing to
        pointer_angle = 90  # Pointer is at top, which is 90 degrees in tkinter (0 is right)
        adjusted_angle = (self.current_angle + pointer_angle) % 360
        section = int(adjusted_angle // self.angle_per_section)
        result = self.numbers[section]
        self.result_label.config(text=f"抽中號碼: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LotteryWheel(root)
    root.mainloop()</content>
<parameter name="filePath">/workspaces/201test0000/lottery_wheel.py