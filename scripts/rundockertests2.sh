# Allow connections from any host
xhost +

docker run -d --name qgis -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /home/jakimowb/Repositories/enmap-box/tests/src/:/tests_directory \
    -e DISPLAY=:99 \
    qgis/qgis:latest

docker exec -it qgis sh -c "cd /tests_directory && qgis_testrunner.sh core.test_enmapbox"