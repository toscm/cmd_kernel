from ipykernel.kernelbase import Kernel
from ipykernel.kernelapp import IPKernelApp
import subprocess as sp

class MyKernel(Kernel):
    implementation = 'tosc_kernel'
    implementation_version = "1.0.0"
    banner = "cmd"
    language_info = {'name': 'python', 'mimetype': 'text/x-python', 'file_extension': '.py'}

    def do_execute(self, code, silent, store_history=True,
                   user_expressions=None, allow_stdin=False):
        output = sp.run(["cmd.exe", "/c", code], capture_output=True).stdout.decode('utf-8')
        stream_content = {'name': 'stdout', 'text': output}
        self.send_response(self.iopub_socket, 'stream', stream_content)
        return {
            'status': 'ok',
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {}
        }


if __name__ == '__main__':
    IPKernelApp.launch_instance(kernel_class=MyKernel)
