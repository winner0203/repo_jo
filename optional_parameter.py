def myself(name, age, nationality = "한국"):
    print("내 이름은 %s" % name)
    print("나이는 %d살" % age)
    print("국적은 %s" % nationality)

myself("코드잇", 1)            # 기본값이 설정된 파라미터를 바꾸지 않을 때
myself("코드잇", 1, "미국")     # 기본값이 설정된 파라미터를 바꾸었을 때