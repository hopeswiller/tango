# comment if you don't wish to use new relic monitoring tool
import newrelic.agent

newrelic.agent.initialize(
    "newrelic.ini", "production", ignore_errors=False, log_file="/var/log/newrelic.log"
)
newrelic.agent.register_application(name="Tango Project")

from tracker import monitor

if __name__ == "__main__":
    monitor.main()
