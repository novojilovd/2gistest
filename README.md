ПРЕДУПРЕЖДЕНИЕ/WARNING Всё исполняется в локальном окружении, рекомендуется использовать на свежесозданных хостах либо скорректировать инфертарный файл и плейбуки

Используются docker_network и docker_containers модули для их использования устанавливаются пакеты pip virtualenv setuptools для соостветствующих систем. (На данный момент только для RedHat)

Поддерживаются Debian и RedHat системы

    Для Debian воспользуйтесь командой ansible-playbook ubuntu.yml
    Для RedHat воспользуйтесь командой ansible-playbook centOS.yml

После выполнения всех задач, войдите в контейнер my_client посредством docker attach

Изменить названия сети, контейнеров и версии Python можно в vars.yml
