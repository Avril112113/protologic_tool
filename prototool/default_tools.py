from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from .prototool import ProtoTool

from .tool import Executable, GithubTool, SystemTool


def add_default_tools(prototool: "ProtoTool"):
	prototool.add_tool(GithubTool("protologic")
		.set_repo("Protologic/Release")
		.set_update_branch(paths=[
			{"Windows": "Sim/Windows", "Linux": "Sim/Linux", "Darwin": "Sim/MacOS"},
			{"Windows": "Player/Windows", "Linux": "Player/Linux", "Darwin": "Player/MacOS"},
		])
		.add_executable(Executable("sim")
			.set_exe({"Windows": "Protologic.Terminal.exe", "Linux": "Protologic.Terminal", "Darwin": "Protologic.Terminal"})
		)
		.add_executable(Executable("player")
			.set_exe({"Windows": "SaturnsEnvy.exe", "Linux": "SaturnsEnvy", "Darwin": "MacOS/SaturnsEnvy"})
		)
	)

	prototool.add_tool(GithubTool("binaryen")
		.set_repo("WebAssembly/binaryen")
		.set_update_release([{"Windows": "x86_64-windows", "Linux": "x86_64-linux", "Darwin": "x86_64-macos"}])
		.add_executable(Executable("wasm2js")
			.set_exe({"Windows": "wasm2js.exe", "Linux": "wasm2js", "Darwin": "wasm2js"})
		)
		.add_executable(Executable("wasm-as")
			.set_exe({"Windows": "wasm-as.exe", "Linux": "wasm-as", "Darwin": "wasm-as"})
		)
		.add_executable(Executable("wasm-ctor-eval")
			.set_exe({"Windows": "wasm-ctor-eval.exe", "Linux": "wasm-ctor-eval", "Darwin": "wasm-ctor-eval"})
		)
		.add_executable(Executable("wasm-dis")
			.set_exe({"Windows": "wasm-dis.exe", "Linux": "wasm-dis", "Darwin": "wasm-dis"})
		)
		.add_executable(Executable("wasm-emsripten-finalize")
			.set_exe({"Windows": "wasm-emsripten-finalize.exe", "Linux": "wasm-emsripten-finalize", "Darwin": "wasm-emsripten-finalize"})
		)
		.add_executable(Executable("wasm-fuzz-lattices")
			.set_exe({"Windows": "wasm-fuzz-lattices.exe", "Linux": "wasm-fuzz-lattices", "Darwin": "wasm-fuzz-lattices"})
		)
		.add_executable(Executable("wasm-fuzz-types")
			.set_exe({"Windows": "wasm-fuzz-types.exe", "Linux": "wasm-fuzz-types", "Darwin": "wasm-fuzz-types"})
		)
		.add_executable(Executable("wasm-merge")
			.set_exe({"Windows": "wasm-merge.exe", "Linux": "wasm-merge", "Darwin": "wasm-merge"})
		)
		.add_executable(Executable("wasm-metadce")
			.set_exe({"Windows": "wasm-metadce.exe", "Linux": "wasm-metadce", "Darwin": "wasm-metadce"})
		)
		.add_executable(Executable("wasm-opt")
			.set_exe({"Windows": "wasm-opt.exe", "Linux": "wasm-opt", "Darwin": "wasm-opt"})
		)
		.add_executable(Executable("wasm-reduce")
			.set_exe({"Windows": "wasm-reduce.exe", "Linux": "wasm-reduce", "Darwin": "wasm-reduce"})
		)
		.add_executable(Executable("wasm-shell")
			.set_exe({"Windows": "wasm-shell.exe", "Linux": "wasm-shell", "Darwin": "wasm-shell"})
		)
		.add_executable(Executable("wasm-split")
			.set_exe({"Windows": "wasm-split.exe", "Linux": "wasm-split", "Darwin": "wasm-split"})
		)
	)

	prototool.add_tool(GithubTool("wizer")
		.set_repo("bytecodealliance/wizer")
		.set_update_release([{"Windows": "x86_64-windows", "Linux": "x86_64-linux", "Darwin": "x86_64-macos"}])
		.add_executable(Executable("wizer")
			.set_exe({"Windows": "wizer.exe", "Linux": "wizer", "Darwin": "wizer"})
		)
	)

	prototool.add_tool(SystemTool("node")
		.add_executable(Executable("node")
			.find_exe("node")
			.set_url("https://nodejs.org/")
			)
			.add_executable(Executable("npm")
				.find_exe("npm")
				.set_url("https://nodejs.org/")
			)
			.add_executable(Executable("npx")
				.find_exe("npx")
				.set_url("https://nodejs.org/")
			)
		)