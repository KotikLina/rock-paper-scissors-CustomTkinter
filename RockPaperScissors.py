from customtkinter import *
from random import randint
import json

with open("RockPaperScissorsConfigure.json") as f:
    data = json.load(f)
SetScaling = data["set scaling"]
ColorTheme = data["color theme"]


class MainWindow(CTk):
    def __init__(self):
        super().__init__()

        self.title("КаменьНожницыБумага")

        self.geometry("450x450")
        self.resizable(False, False)

        deactivate_automatic_dpi_awareness()
        set_widget_scaling(SetScaling)  # widget dimensions and text size
        set_window_scaling(SetScaling)  # window geometry dimensions
        set_appearance_mode(ColorTheme)

        self.font1 = CTkFont(size=30, weight="bold")
        self.font2 = CTkFont(size=25, weight="bold")

        # Фрейм для отображения названия игры и её версии
        self.FrameName = CTkFrame(master=self, fg_color=("#2d9bf1", "#1f6aa5"))
        self.FrameName.pack(pady=30)

        # Лабельки для отображения названия игры и её версии
        self.NameGame = CTkLabel(master=self.FrameName, text="КаменьНожницыБумага", text_color="white",
                                 font=self.font1)
        self.NameGame.pack(padx=10, pady=(10, 5))

        self.VersionGame = CTkLabel(master=self.FrameName, text="CustomTkinter Edition 2.0", text_color="white",
                                    font=self.font1)
        self.VersionGame.pack(padx=10, pady=(5, 10))

        # Фрейм для главных кнопок
        self.FrameMainMenu = CTkFrame(master=self, fg_color=("#b7b7b7", "#404040"))
        self.FrameMainMenu.pack(pady=10)

        # Кнопки главного меню
        self.ButtonStartGame1 = CTkButton(master=self.FrameMainMenu, text="Играть", font=self.font2,
                                          command=self.OpenGameWindow)
        self.ButtonStartGame1.grid(row=0, column=0, ipadx=40, ipady=2, padx=20, pady=(20, 10), sticky="nswe")
        self.ButtonStartGame2 = CTkButton(master=self.FrameMainMenu, text="Настройки", font=self.font2,
                                          command=self.OpenSettingWindow)
        self.ButtonStartGame2.grid(row=2, column=0, ipadx=30, ipady=2, padx=20, pady=(10, 10), sticky="nswe")
        self.ButtonStartGame3 = CTkButton(master=self.FrameMainMenu, text="Выход", font=self.font2,
                                          command=self.CloseWindow)
        self.ButtonStartGame3.grid(row=3, column=0, ipadx=40, ipady=2, padx=20, pady=(10, 20), sticky="nswe")

        # Переменные для окон
        self.toplevel_gameWindow = None
        self.toplevel_settingWindow = None

    # Методы для кнопок
    def OpenGameWindow(self):
        if self.toplevel_gameWindow is None or not self.toplevel_gameWindow.winfo_exists():
            self.toplevel_gameWindow = PlayWindow(focus=True)  # create window if its None or destroyed
        else:
            self.toplevel_gameWindow.focus()  # if window exists focus it

    def OpenSettingWindow(self):
        if self.toplevel_settingWindow is None or not self.toplevel_settingWindow.winfo_exists():
            self.toplevel_settingWindow = SettingWindow(focus=True)  # create window if its None or destroyed
        else:
            self.toplevel_settingWindow.focus()  # if window exists focus it

    def CloseWindow(self):
        self.after(100, self.destroy)


class SettingWindow(CTkToplevel):
    def __init__(self, focus=False):
        super().__init__()
        if focus:
            self.after(250, self.focus_force)

        self.title("КаменьНожницыБумага")

        self.geometry("450x350")
        self.resizable(False, False)

        deactivate_automatic_dpi_awareness()
        set_widget_scaling(SetScaling)  # widget dimensions and text size
        set_window_scaling(SetScaling)  # window geometry dimensions
        set_appearance_mode(ColorTheme)

        self.font1 = CTkFont(size=30, weight="bold")
        self.font2 = CTkFont(size=16, weight="bold")
        self.font3 = CTkFont(size=16)

        # Фрейм для отображения названия игры и её версии
        self.FrameName = CTkFrame(master=self, fg_color=("#2d9bf1", "#1f6aa5"))
        self.FrameName.pack(pady=30)

        # Лабельки для отображения названия игры и её версии
        self.NameGame = CTkLabel(master=self.FrameName, text="КаменьНожницыБумага", text_color="white",
                                 font=self.font1)
        self.NameGame.pack(padx=10, pady=(10, 5))

        self.VersionGame = CTkLabel(master=self.FrameName, text="CustomTkinter Edition 2.0", text_color="white",
                                    font=self.font1)
        self.VersionGame.pack(padx=10, pady=(5, 10))

        # Фрейм для всего
        self.Frame = CTkFrame(master=self, fg_color=("#b7b7b7", "#404040"))
        self.Frame.pack()

        # Свич для изменения отображения статистики матчей по-умолчанию
        self.SwitchForScoringByDefault = CTkSwitch(master=self.Frame, text="Отображение статистики по-умолчанию",
                                                   command=self.FuncForScoringByDefault,
                                                   font=self.font2)
        self.SwitchForScoringByDefault.grid(row=0, column=0, padx=10, pady=(10, 10))
        if data["statistics display"]:
            self.SwitchForScoringByDefault.toggle()

        # Фрейм для изменения темы и размера.
        self.FrameForScaling = CTkFrame(master=self.Frame, fg_color=("#9e9e9e", "#191919"))
        self.FrameForScaling.grid(row=1, column=0, pady=10, padx=10)

        # Лабельки для слов
        self.Label1 = CTkLabel(master=self.FrameForScaling, fg_color=("#9e9e9e", "#191919"), text="set scaling",
                               font=self.font3)
        self.Label1.grid(row=0, column=0, padx=10, pady=5)

        self.Label2 = CTkLabel(master=self.FrameForScaling, fg_color=("#9e9e9e", "#191919"), text="default color theme",
                               font=self.font3)
        self.Label2.grid(row=0, column=3, padx=10, pady=5)

        # Опциональные меню для изменения appearance mode и default color theme
        self.OptionMenuAppearanceMode = CTkOptionMenu(master=self.FrameForScaling,
                                                      values=["80%", "90%", "100%", "110%", "120%"],
                                                      command=self.ChangeScalingEvent)
        self.OptionMenuAppearanceMode.grid(row=1, column=0, padx=10, pady=(0, 10))
        PercentSetScaling = str(int(SetScaling * 100)) + "%"
        self.OptionMenuAppearanceMode.set(PercentSetScaling)

        self.OptionMenuDefaultColorTheme = CTkOptionMenu(master=self.FrameForScaling,
                                                         values=["Light", "Dark", "System"],
                                                         command=self.ChangeAppearanceModeEvent)
        self.OptionMenuDefaultColorTheme.grid(row=1, column=3, padx=10, pady=(0, 10))
        self.OptionMenuDefaultColorTheme.set(ColorTheme)

    def FuncForScoringByDefault(self):
        if self.SwitchForScoringByDefault.get():
            data["statistics display"] = True
            with open("four_words.json", "w") as file:
                json.dump(data, file, indent=4)
        else:
            data["statistics display"] = False
            with open("four_words.json", "w") as file:
                json.dump(data, file, indent=4)

    @staticmethod
    def ChangeScalingEvent(new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        data["set scaling"] = new_scaling_float
        with open("four_words.json", "w") as file:
            json.dump(data, file, indent=4)
        set_widget_scaling(new_scaling_float)
        set_window_scaling(new_scaling_float)

    @staticmethod
    def ChangeAppearanceModeEvent(new_appearance_mode: str):
        data["color theme"] = new_appearance_mode
        with open("four_words.json", "w") as file:
            json.dump(data, file, indent=4)
        set_appearance_mode(new_appearance_mode)


class PlayWindow(CTkToplevel):
    def __init__(self, focus=False):
        super().__init__()
        if focus:
            self.after(250, self.focus_force)  # Call focus_force() after 250ms

        self.scoring = Scoring(self)
        self.game = Game(self)

        self.title("КаменьНожницыБумага")

        if data["statistics display"]:
            self.armature = 1
            self.geometry("550x600")
        else:
            self.armature = 0
            self.geometry("550x450")
        self.resizable(False, False)

        deactivate_automatic_dpi_awareness()
        set_widget_scaling(SetScaling)  # widget dimensions and text size
        set_window_scaling(SetScaling)  # window geometry dimensions
        set_appearance_mode(ColorTheme)

        self.font1 = CTkFont(size=30, weight="bold")
        self.font2 = CTkFont(size=16, weight="bold")
        self.font3 = CTkFont(size=16)

        # Фрейм для отображения названия игры и её версии
        self.FrameName = CTkFrame(master=self, fg_color=("#2d9bf1", "#1f6aa5"))
        self.FrameName.pack(pady=30)

        # Лабельки для отображения названия игры и её версии
        self.NameGame = CTkLabel(master=self.FrameName, text="КаменьНожницыБумага", text_color="white",
                                 font=self.font1)
        self.NameGame.pack(padx=10, pady=(10, 5))

        self.VersionGame = CTkLabel(master=self.FrameName, text="CustomTkinter Edition 2.0", text_color="white",
                                    font=self.font1)
        self.VersionGame.pack(padx=10, pady=(5, 10))

        # Фрейм для всего
        self.Frame = CTkFrame(master=self, fg_color=("#b7b7b7", "#404040"))
        self.Frame.pack()

        # Фрейм для отображения выбора человека и компьютера
        self.FrameChoice = CTkFrame(master=self.Frame, fg_color=("#9e9e9e", "#191919"))
        self.FrameChoice.grid(row=0, column=0, padx=100, pady=(15, 10), sticky="nswe")

        # Лабелька для отображения противников
        self.LabelChoice1 = CTkLabel(master=self.FrameChoice, text="Человек", font=self.font2,
                                     fg_color=("#9e9e9e", "#191919"))
        self.LabelChoice1.pack(side="left", pady=3, padx=5)
        self.LabelChoice2 = CTkLabel(master=self.FrameChoice, text=" против ", font=self.font2,
                                     fg_color=("#9e9e9e", "#191919"))
        self.LabelChoice2.pack(side='left', expand=True, pady=3, padx=5)
        self.LabelChoice3 = CTkLabel(master=self.FrameChoice, text="Компьютера", font=self.font2,
                                     fg_color=("#9e9e9e", "#191919"))
        self.LabelChoice3.pack(side="right", pady=3, padx=5)

        # Фрейм для отображения результата поединка
        self.FrameResultBattle = CTkFrame(master=self.Frame, fg_color=("#9e9e9e", "#191919"))
        self.FrameResultBattle.grid(row=1, column=0, padx=100, sticky="nswe")

        # Лабельки для отображения результата поединка
        self.LabelResultBattle = CTkLabel(master=self.FrameResultBattle, text="Результат матча", font=self.font1,
                                          text_color="white", width=150)
        self.LabelResultBattle.pack(pady=5, padx=10)

        # Фрейм для отображения кнопок выбора игрока
        self.FrameButtonsToSelect = CTkFrame(master=self.Frame, fg_color=("#9e9e9e", "#191919"), width=150)
        self.FrameButtonsToSelect.grid(row=2, column=0, pady=(10, 15), padx=15)

        # Лабельки для отображения кнопок выбора игрока
        self.LabelButtonsToSelect1 = CTkButton(master=self.FrameButtonsToSelect, text="Камень", font=self.font1,
                                               width=100, command=lambda: self.game.round_result_calculation(0))
        self.LabelButtonsToSelect1.grid(row=0, column=0, padx=7, pady=7)

        self.LabelButtonsToSelect2 = CTkButton(master=self.FrameButtonsToSelect, text="Ножницы", font=self.font1,
                                               width=100, command=lambda: self.game.round_result_calculation(1))
        self.LabelButtonsToSelect2.grid(row=0, column=1, padx=0, pady=7)

        self.LabelButtonsToSelect3 = CTkButton(master=self.FrameButtonsToSelect, text="Бумага", font=self.font1,
                                               width=100, command=lambda: self.game.round_result_calculation(2))
        self.LabelButtonsToSelect3.grid(row=0, column=2, padx=7, pady=7)

        # Фрейм для отображения статистики матчей
        self.FrameScoring = CTkFrame(master=self, fg_color=("#b7b7b7", "#404040"))
        self.FrameScoring.pack(pady=10)

        # Фрейм для свича отображения статистики матчей
        self.FrameSwitchForScoring = CTkFrame(master=self.FrameScoring, fg_color=("#b7b7b7", "#404040"))
        self.FrameSwitchForScoring.grid(row=0, column=0, padx=10)

        # Свич для отображения статистики матчей
        self.SwitchForScoring = CTkSwitch(master=self.FrameSwitchForScoring, text="Отобразить подсчёт очков",
                                          font=self.font3)
        self.SwitchForScoring.grid(padx=10, pady=9)
        self.SwitchForScoring.bind('<Button-1>', lambda event: self.ToggleFrameResults())

        # Фрейм для кнопки, которая добавит функцию "стереть статистику"
        self.FrameEraseScoringButton = CTkFrame(master=self.FrameScoring, fg_color=("#b7b7b7", "#404040"))
        self.FrameEraseScoringButton.grid(row=0, column=1, padx=10)

        # Кнопка, чтобы стереть статистику
        self.EraseScoringButton = CTkButton(master=self.FrameEraseScoringButton, text="Стереть", font=self.font3,
                                            width=40, bg_color=("#b7b7b7", "#404040"),
                                            command=self.scoring.erase_scoring,
                                            state="disabled")
        self.EraseScoringButton.pack(pady=(6, 5))

        # Фрейм для отображения результатов всех игр
        self.FrameResults = CTkFrame(master=self.FrameScoring, fg_color=("#9e9e9e", "#191919"))

        # Лабельки для отображения результатов всех игр
        self.LabelTextResults = CTkLabel(master=self.FrameResults, text="Результаты матчей", font=self.font1, height=30)
        self.LabelTextResults.pack(padx=10, pady=5)

        self.LabelWinResults = CTkLabel(master=self.FrameResults, text="Количество побед: 0", font=self.font2,
                                        width=230)
        self.LabelWinResults.pack()

        self.LabelLoseResults = CTkLabel(master=self.FrameResults, text="Количество поражений: 0", font=self.font2,
                                         width=230)
        self.LabelLoseResults.pack()

        self.LabelDrawResults = CTkLabel(master=self.FrameResults, text="Количество ничьих: 0", font=self.font2,
                                         width=230)
        self.LabelDrawResults.pack()

        # Отображение статистики по-умолчанию
        if data["statistics display"]:
            self.SwitchForScoring.toggle()
            self.FrameResults.grid(row=1, column=0, columnspan=2, pady=15, padx=15, ipady=3)
            self.EraseScoringButton.configure(state="enabled")

    def ToggleFrameResults(self):
        if self.SwitchForScoring.get():
            self.armature = 1
            self.FrameResults.grid(row=1, column=0, columnspan=2, pady=15, padx=15, ipady=3)
            self.EraseScoringButton.configure(state="enabled")
            self.geometry("550x600")
        else:
            self.armature = 0
            self.scoring.erase_scoring()
            self.geometry("550x450")
            self.FrameResults.grid_forget()
            self.EraseScoringButton.configure(state="disabled")


class Game:
    def __init__(self, play_window):
        self.play_window = play_window

    CHOICES = ["камень", "ножницы", "бумага"]
    RESULTS = ["Ничья", "Поражение", "Победа"]

    def round_result_calculation(self, player_choice):
        computer_choice = randint(0, 2)
        result = (player_choice - computer_choice) % 3

        self.player_choices(player_choice, computer_choice)
        self.return_result_round(result)
        if self.play_window.armature:
            self.sending_for_scoring(result)

    def player_choices(self, player_choice, computer_choice):
        self.play_window.LabelChoice1.configure(text=f"{Game.CHOICES[player_choice]}")
        self.play_window.LabelChoice3.configure(text=f"{Game.CHOICES[computer_choice]}")

    def return_result_round(self, result):
        self.play_window.LabelResultBattle.configure(text=Game.RESULTS[result])

    def sending_for_scoring(self, result):
        resultsDictionary = {
            0: self.play_window.scoring.scoring_draws,
            1: self.play_window.scoring.scoring_lose,
            2: self.play_window.scoring.scoring_wins}
        resultsDictionary[result]()


class Scoring:
    def __init__(self, play_window):
        self.play_window = play_window

        self.all = 0
        self.wins = 0
        self.lose = 0
        self.draws = 0

    # счётчик побед
    def scoring_wins(self):
        self.all += 1
        self.wins += 1
        self.play_window.LabelWinResults.configure(text=f"Побед: {self.wins}")

    # счётчик поражений
    def scoring_lose(self):
        self.all += 1
        self.lose += 1
        self.play_window.LabelLoseResults.configure(text=f"Поражений: {self.lose}")

    # счётчик партий, закончившихся ничьей
    def scoring_draws(self):
        self.all += 1
        self.draws += 1
        self.play_window.LabelDrawResults.configure(text=f"Ничейныйх партий: {self.draws}")

    def erase_scoring(self):
        self.all = 0
        self.wins = 0
        self.lose = 0
        self.draws = 0
        self.play_window.LabelWinResults.configure(text=f"Побед: {self.wins}")
        self.play_window.LabelLoseResults.configure(text=f"Поражений: {self.lose}")
        self.play_window.LabelDrawResults.configure(text=f"Ничейныйх партий: {self.draws}")


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
