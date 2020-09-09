#!/bin/sh
"/opt/pycharm-community-2019.3.3/jbr/bin/java" -cp "/opt/pycharm-community-2019.3.3/plugins/git4idea/lib/git4idea-rt.jar:/opt/pycharm-community-2019.3.3/lib/xmlrpc-2.0.1.jar:/opt/pycharm-community-2019.3.3/lib/commons-codec-1.13.jar:/opt/pycharm-community-2019.3.3/lib/util.jar" org.jetbrains.git4idea.nativessh.GitNativeSshAskPassApp "$@"
