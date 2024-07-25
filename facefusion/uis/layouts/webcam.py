import gradio

from facefusion import state_manager
from facefusion.uis.components import about, execution, execution_thread_count, processors, processors_options, source, webcam, webcam_options


def pre_check() -> bool:
	return True


def pre_render() -> bool:
	return True


def render() -> gradio.Blocks:
	with gradio.Blocks() as layout:
		with gradio.Row():
			with gradio.Column(scale = 2):
				with gradio.Blocks():
					about.render()
				with gradio.Blocks():
					processors.render()
				with gradio.Blocks():
					processors_options.render()
				with gradio.Blocks():
					execution.render()
					execution_thread_count.render()
				with gradio.Blocks():
					webcam_options.render()
				with gradio.Blocks():
					source.render()
			with gradio.Column(scale = 5):
				with gradio.Blocks():
					webcam.render()
	return layout


def listen() -> None:
	processors.listen()
	processors_options.listen()
	execution.listen()
	execution_thread_count.listen()
	source.listen()
	webcam.listen()


def run(ui : gradio.Blocks) -> None:
	ui.launch(show_api = False, inbrowser = state_manager.get_item('open_browser'))
