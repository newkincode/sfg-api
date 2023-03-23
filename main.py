import pygame
import json
import datetime

if __name__ == "__main__":
    pygame.init()
    # runtime values
    from lib import runtime_values
    from lib import player

    runtime_values.players = [player.Player(pygame.image.load(
        "assets/img/player.png"), pygame.math.Vector2(900, 100), runtime_values.screen, runtime_values.window_size)]

    # 셋팅파일 열기
    with open("data/setting.json", 'r', encoding='utf8') as setting_file:
        runtime_values.setting = json.load(setting_file)
    # 언어파일 열기
    with open(f"data/lang/{runtime_values.setting['lang']}.json", 'r', encoding='utf8') as lang_file:
        runtime_values.lang = json.load(lang_file)

    runtime_values.running = True
    runtime_values.my_dir = player.Direction.STOP
    runtime_values.start_time = datetime.datetime.now()
    runtime_values.logs = []

    # 버전변수
    version = runtime_values.version
    version_text = f"{version[0]} {version[1]}.{version[2]}.{version[3]}"

    from lib import draw
    from lib import keyinput
    from lib import farm
    from lib import logger
    from lib import imgs
    from lib.plants import plants_list
    from lib import importmod

    print(f'''
                         _    ___       ___
     _ __   _____      _| | _|_ _|_ __ |_ _|
    | '_ \\ / _ \\ \\ /\\ / / |/ /| || '_ \\ | |
    | | | |  __/\\ V  V /|   < | || | | || |
    |_| |_|\\___| \\_/\\_/ |_|\\_\\___|_| |_|___| Games
     ____         _____         ____
    / ___|       |  ___|       / ___|
    \\___ \\       | |_         | |  _
     ___) |      | _|         | |_| |
    |____/ imple |_|  arming   \\____|ame
    
    V. {version_text}
    ''', end="")
    logger.log_info("Start Loading")

    # 변수
    # colors
    SKYBLUE = pygame.Color(113, 199, 245)
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    # 폰트
    font_renderer = pygame.font.Font("assets/font/Galmuri.ttf", 20)
    # 노래
    musics: dict[str, pygame.mixer.Sound] = {
        "sfg": pygame.mixer.Sound("assets/music/sfg.mp3")
    }

    # 세팅
    pygame.display.set_caption(f"sfg {version_text}! - by newkini")
    pygame.display.set_icon(pygame.image.load('assets/img/icon.png'))
    pygame.mouse.set_visible(False)
    if runtime_values.setting["musicStart"]:
        musics["sfg"].play()

    # 게임와일
    logger.log_info("Finish Loading")
    while runtime_values.running:
        musPos: tuple = pygame.mouse.get_pos()
        df = runtime_values.clock.tick(runtime_values.fps) / 1000
        runtime_values.clock.tick(runtime_values.fps)
        # 그리기
        # 화면
        runtime_values.screen.fill(SKYBLUE)  # 화면 채우기
        draw.draw_ground(runtime_values.screen)
        # 그외
        draw.draw_plants()  # 식물
        draw.draw_players()  # 플래이어
        # 글시
        draw.draw_text_with_border(  # 버전명
            runtime_values.screen, font_renderer, f"SFG {version_text}!  {runtime_values.lang['guid']}", WHITE, BLACK, 2, pygame.math.Vector2(10, 10))
        draw.draw_text_with_border(  # 좌표
            runtime_values.screen, font_renderer, str(runtime_values.players[0].get_tile_pos()), WHITE, BLACK, 2, pygame.math.Vector2(850, 35))
        draw.draw_text_with_border(  # 셀렉트 아이템
            runtime_values.screen, font_renderer, runtime_values.lang["select"]+" : " + \
            runtime_values.lang["items"][runtime_values.players[0].handle_item.name],
            WHITE, BLACK, 2, pygame.math.Vector2(10, 35))
        if runtime_values.players[0].handle_item in plants_list.plants_list or runtime_values.players[0].handle_item.name == "VITAMIN":  # type: ignore
            draw.draw_text_with_border(  # 아이템 겟수
                runtime_values.screen, font_renderer, runtime_values.lang["count"]+" : "+str(runtime_values.players[0].inventory[runtime_values.players[0].handle_item.name]) +
                " seed : "+str({runtime_values.players[0].inventory[f"{runtime_values.players[0].handle_item.name}_seed"]}), WHITE, BLACK, 2, pygame.math.Vector2(10, 60))
        draw.draw_text_with_border(  # 좌표
            runtime_values.screen, font_renderer, "gold : "+str({runtime_values.players[0].inventory["gold"]}), WHITE, BLACK, 2, pygame.math.Vector2(10, 85))

        runtime_values.screen.blit(imgs.img("mus"), musPos)  # 마우스 커서

        # 처리
        keyinput.process()
        runtime_values.players[0].move(runtime_values.my_dir, df)
        farm.process_plants()
        pygame.display.update()  # 화면 업데이트

    logger.log_info("quit")
    logger.save(runtime_values.start_time)
    musics["sfg"].stop()
    pygame.quit()
