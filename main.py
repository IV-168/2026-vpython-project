Web VPython 3.2

#  일단 총부터 먼저 제작해야함. 
tp = box(color = vec(0.3,0.3,0.3), size = vec(8,1,1))
p1per = cylinder(pos = vec(-0.85, 0, 0), axis = vec(5, 0, 0), radius = 0.35, color = vec(224/255, 224/255, 224/255))
box(color = vec(0.15,0.15,0.15), size = vec(8,1,1), pos = vec(0,-1,0))
grip = box(color = vec(0.15,0.15,0.15), size = vec(2,4,1), pos = vec(-2.25,-2,0))
box(color = vec(0.15,0.15,0.15), size = vec(0.4,1,0.5), pos = vec(0,-2,0))
box(color = vec(0.15,0.15,0.15), size = vec(1.4,0.5,0.5), pos = vec(-0.7,-2.25,0))
trigger = box(color = vec(0.15,0.15,0.15), size = vec(0.5,0.25,0.25), pos = vec(-0.85,-1.65,0)) #방아쇠를 trigger라고 저장하고 별도로 기울여야 함
trigger.rotate(angle = radians(135), axis=vec(0,0,1))
grip.rotate(angle = radians(345), axis=vec(0,0,1))

# 이제 총 모양 다 잡았으니 총알 발사 ㄱㄱ
bullets = []
remainingbullets = 18

while True:
    rate(100)
    k = keysdown()
    if ' ' in k:
        if remainingbullets > 0:
            bullets.append(box(pos = vec(-3, 0, 0), size = vec(0.5, 0.5, 0.5), texture = "https://i.postimg.cc/13Smbq5d/Pngtreebullet-isolated-on-transparent-background-21133552-(1)-(1).png"))
            remainingbullets = remainingbullets - 1
            
        
    if 'r' in k: # 재장전
        tp.pos.x = tp.pos.x - 2
        remainingbullets = 18
        sleep(1)
        tp.pos.x = tp.pos.x + 2
        
    for i in bullets:
        i.pos.x = i.pos.x + 1
