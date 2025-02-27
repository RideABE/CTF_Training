# 2025-02-10 题单

## 今日主题关键词

新手，reverse，语言逆向，pwn，栈溢出

## 今日题目

- [x] 20金币 [HGAME 2023 week1]test_nc https://www.nssctf.cn/problem/3487 

- [ ] 20金币 [SWPUCTF 2024 秋季新生赛]又是签到！？ https://www.nssctf.cn/problem/5934 

- [ ] 10金币 [WUSTCTF 2020]level1 https://www.nssctf.cn/problem/1996 
- [ ] 15金币 [SWPUCTF 2022 新生赛]FindanotherWay https://www.nssctf.cn/problem/2783 
- [ ] 20金币 [HNCTF 2022 WEEK4]checker https://www.nssctf.cn/problem/3106

## 题解

### [HGAME 2023 week1]test_nc

#### 题目描述

test_nc

#### 题解

- 我们开启环境以后直接使用nc工具连接主机

```bash
nc nc node5.anna.nssctf.cn 25460
```

- 然后我们进行ls，得到文件目录，找到flag文件直接cat得到答案

```bash
ls
bin
dev
flag
lib
lib32
lib64
libx32
vuln
cat flag
NSSCTF{b5b37278-cbe3-4e91-9046-b0ce46d8065c}
```

#### 答案

```
NSSCTF{b5b37278-cbe3-4e91-9046-b0ce46d8065c}
```

### [SWPUCTF 2024 秋季新生赛]又是签到！？

#### 题目描述

一个.apk文件

#### 题解

- 我们开启环境以后直接使用nc工具连接主机

```bash
nc nc node5.anna.nssctf.cn 25460
```
