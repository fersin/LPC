#!/bin/bash
myf () {
        while :
        do
                echo "hola $1"
                echo "ingrese su edad "
                read v
                echo "hola su edad es $v"
                if [[ $v -lt 18 ]]
                then
                        echo "usted no tiene edad para esto "
                else
                        echo "pasele :)"
                fi
                echo "desea continuar? 1 para si o presione CTRL+C "
                read c
                if [[ $c -eq 1 ]]
                then
                        continue
                fi
        done
}
myf $1
