import os
import re
import pygame

from code.Consts import WIN_WIDTH, WIN_HEIGHT

class Background():
    def __init__(self, window, path_image, phase_duration=30):
        self.window = window
        self.single = False
        self.phase_duration_ms = int(phase_duration * 1000)

        parent_dir = path_image if os.path.isdir(path_image) else os.path.dirname(path_image)
        parent_name = os.path.basename(parent_dir)

        m = re.match(r"^(.+?)\s*(\d+)$", parent_name)
        base_prefix = m.group(1).strip() if m else parent_name

        grandparent = os.path.dirname(parent_dir)

        candidate_dirs = []
        try:
            for name in sorted(os.listdir(grandparent)):
                full = os.path.join(grandparent, name)
                if not os.path.isdir(full):
                    continue
                mm = re.match(rf"^{re.escape(base_prefix)}\s*(\d+)$", name)
                if mm:
                    candidate_dirs.append((int(mm.group(1)), full))
        except Exception:
            candidate_dirs = []

        candidate_dirs.sort(key=lambda t: t[0])
        background_dirs = [t[1] for t in candidate_dirs]

        if not background_dirs:
            background_dirs = [parent_dir]

        self.background_sets = []  # cada item: list of {'surf': Surface, 'speed': float}
        base_speeds = [0.3, 0.6, 0.9, 1.2, 1.6, 2.0]

        for bdir in background_dirs:
            numeric_files = []
            try:
                for name in sorted(os.listdir(bdir)):
                    base, ext = os.path.splitext(name)
                    if ext.lower() == '.png' and base.isdigit():
                        numeric_files.append(os.path.join(bdir, name))
            except Exception:
                numeric_files = []

            if numeric_files:
                layer_defs = []
                for i, fpath in enumerate(numeric_files):
                    surf = pygame.image.load(fpath).convert_alpha()
                    surf = pygame.transform.scale(surf, (WIN_WIDTH, WIN_HEIGHT))
                    speed = base_speeds[i] if i < len(base_speeds) else base_speeds[-1] * (1.0 + 0.2 * (i - len(base_speeds) + 1))
                    layer_defs.append({'surf': surf, 'speed': float(speed)})
                self.background_sets.append(layer_defs)
            else:
                pass

        if not self.background_sets:
            self.single = True
            try:
                self.image = pygame.image.load(path_image).convert()
                self.image = pygame.transform.scale(self.image, (WIN_WIDTH, WIN_HEIGHT))
                self.scroll_speed = 1
            except Exception:
                self.image = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
                self.image.fill((0, 0, 0))
            return

        try:
            start_index = background_dirs.index(parent_dir) if parent_dir in background_dirs else 0
        except Exception:
            start_index = 0
        self.current_index = start_index
        self._instantiate_current_layers()
        self.phase_start = pygame.time.get_ticks()

    def _instantiate_current_layers(self):
        base = self.background_sets[self.current_index]
        self.layers = []
        for defn in base:
            self.layers.append({'surf': defn['surf'], 'pos': [0.0, float(WIN_WIDTH)], 'speed': defn['speed']})

    def update(self):
        if self.single:
            return

        now = pygame.time.get_ticks()
        if now - self.phase_start >= self.phase_duration_ms:
            self.current_index = (self.current_index + 1) % len(self.background_sets)
            self._instantiate_current_layers()
            self.phase_start = now

        for layer in self.layers:
            for i in range(len(layer['pos'])):
                layer['pos'][i] -= layer['speed']
                if layer['pos'][i] <= -WIN_WIDTH:
                    layer['pos'][i] += WIN_WIDTH * 2

    def draw(self):
        if self.window is None:
            return

        if self.single:
            self.window.blit(self.image, (0, 0))
            return

        for layer in self.layers:
            surf = layer['surf']
            for x in layer['pos']:
                self.window.blit(surf, (int(x), 0))
