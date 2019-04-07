export SRC_DIR=src
export PYTHON_DIR=python
export RUBY_DIR=ruby
export C_DIR=c
export JAVA_DIR=java
protoc -I=$SRC_DIR --python_out=$PYTHON_DIR $SRC_DIR/midimessage.proto
protoc -I=$SRC_DIR --ruby_out=$RUBY_DIR $SRC_DIR/midimessage.proto
cp python/* ../python
cp ruby/* ~/DawRuby/EventLoop
