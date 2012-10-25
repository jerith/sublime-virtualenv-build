import os

import sublime_plugin


class VirtualenvExecCommand(sublime_plugin.WindowCommand):
    def run(self, working_dir="", path=None, virtualenv_dir=None, **kwargs):
        view_settings = self.window.active_view().settings()
        working_dir = view_settings.get("build_working_dir", working_dir)

        if virtualenv_dir is None:
            virtualenv_dir = view_settings.get("virtualenv_dir")

        venv_bin_path = os.path.join(virtualenv_dir, "bin")

        if path is not None:
            path = os.pathsep.join([path, venv_bin_path])
        else:
            path = venv_bin_path

        kwargs["working_dir"] = working_dir
        kwargs["path"] = path

        return self.window.run_command("exec", kwargs)
