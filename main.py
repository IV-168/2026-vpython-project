Web VPython 3.2

#  일단 총부터 먼저 제작해야함. 
box(color = vec(0.3,0.3,0.3), size = vec(8,1,1))
box(color = vec(0.15,0.15,0.15), size = vec(8,1,1), pos = vec(0,-1,0))
grip = box(color = vec(0.15,0.15,0.15), size = vec(2,4,1), pos = vec(-2.25,-2,0))
box(color = vec(0.15,0.15,0.15), size = vec(0.4,1,0.5), pos = vec(0,-2,0))
box(color = vec(0.15,0.15,0.15), size = vec(1.25,0.5,0.5), pos = vec(-0.65,-2.25,0))
trigger = box(color = vec(0.15,0.15,0.15), size = vec(0.5,0.25,0.25), pos = vec(-0.6,-1.65,0)) #방아쇠를 trigger라고 저장하고 별도로 기울여야 함
trigger.rotate(angle = radians(135), axis=vec(0,0,1))
grip.rotate(angle = radians(345), axis=vec(0,0,1))
