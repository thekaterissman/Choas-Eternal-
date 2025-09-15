class AIBody:
    def __init__(self, renderer):
        self.renderer = renderer
        self.is_manifested = False

    def manifest(self):
        if not self.is_manifested:
            self.renderer.render_ai_body()
            self.is_manifested = True

    def disappear(self):
        if self.is_manifested:
            self.renderer.unrender_ai_body()
            self.is_manifested = False
