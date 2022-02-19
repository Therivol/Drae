import ui


class UnitFrame:
    def __init__(self, game, entity):
        self.entity = entity

        self.components = []
        self.health_bg = ui.background.Background(game, (0.115, 0.053), (0.14, 0.066), (0, 0, 0))
        self.static_health = ui.background.Background(game, (0.115, 0.053), (0.13, 0.056), (150, 0, 0))
        self.health_text = ui.text.Text(game, (0.115, 0.053), f"{entity.health.current}/{entity.health.maximum}", 32, (255, 255, 255))

        self.components.append(self.health_bg)
        self.components.append(self.static_health)
        self.components.append(self.health_text)

    def update(self, dt):
        pass

    def render(self, display):
        for comp in self.components:
            comp.render(display)
