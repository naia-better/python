import cards_tools
# 无限循环，由用户自己决定什么时候退出循环
while True:
    # TODO 显示功能菜单
    cards_tools.show_menu()

    action_str = input("请输入要执行的操作：")

    print("你选择的操作是 【%s】" % action_str)

    # 1,2,3 名片操作
    if action_str in ["1","2","3"]:

        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示名片
        elif action_str == "2":
            cards_tools.show_all()
        # 查询名片
        elif action_str == "3":
            cards_tools.search_card()


    # 0 退出系统
    elif action_str == "0":

        print("欢迎再次使用【名片管理系统】")
        break
    # 输入不正确，请重新输入
    else:
        print("输入有误，重新输入：")




