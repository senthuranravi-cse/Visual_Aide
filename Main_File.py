print("""...........Welcome..........\n1.Magnifier\n2.Draw in Present Screen\n3.Notepad\n4.More Features\n""")
while True:
    n=int(input("Enter Your Option:"))
    if n==4:
        import Features as d
        d.main1()
    if n==1:
       print("If you want to close Magnifier just press ""ESC""")
       import mag as m
       m.main11()
    if n==2:
        print("Pen will Activate in 5 Sec...please open tab where you want to write")
        import Screen_Drawer as s
        s.main()
    if n==3:
        import Notepad as n
        n.main()
