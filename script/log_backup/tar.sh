#!/usr/bin/env bash

# 文件夹  201710 201708 201709
for tgz in 201710 201708 201709
        do
        tar zcvf $tgz.tar.gz  $tgz
done
