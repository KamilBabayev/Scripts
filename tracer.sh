#!/bin/bash
# I have wrote this script to automate tracing remote services in order to make 
# it quick when requested, not to lose time to find details of service every time

trace_service01(){
    tracefile="/tmp/service01_trace_$(date +%F).pcap"
    tcpdump -i any -nn host 10.10.10.11 -w $tracefile
    echo "Result has been saved to -> " $tracefile
}
trace_service02(){
    tracefile="/tmp/service02_trace_$(date +%F).pcap"
    tcpdump -i any -nn host 10.10.10.12 -w $tracefile
    echo "Result has been saved to -> " $tracefile
}


echo "Which one to trace ?"
select i in service01 service02
do
    case $i in
        service01)
            echo "Tracing Service01.... press Ctrl+C when you want to stop"
            trace_service01
            exit 0
            ;;
        service02)
            echo "Tracing Service02.... press Ctrl+C when you want to stop"
            trace_service02
            exit 0
            ;;
    esac
done

