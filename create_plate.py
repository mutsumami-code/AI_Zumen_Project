import ezdxf

doc = ezdxf.new("R2010")
msp = doc.modelspace()

# 外形（170×80）
points = [
    (10, 0),
    (160, 0),
    (170, 10),
    (170, 70),
    (160, 80),
    (10, 80),
    (0, 70),
    (0, 10),
]

msp.add_lwpolyline(points, close=True)

# 穴 φ20
msp.add_circle((85, 40), 10)

# 穴 φ10
msp.add_circle((35, 40), 5)
msp.add_circle((135, 40), 5)

doc.saveas("plate.dxf")

print("DXFを作成しました。")
