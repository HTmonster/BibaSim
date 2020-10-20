### Biba模型模拟

> 对完整性安全模型biba的模拟实现
>
> 技术栈：Flask+Vue(element)

#### 一. Biba模型概念

##### 1. 背景信息

> BLP模型保证的是数据机密性，是军事安全模型。而商业应用中人们往往关心的是数据的完整性。

- Biba等人
- 1977年提出的第一个完整性安全模型

##### 2.简单介绍

- 为系统中每一个**主体**和**客体**分配一个完整性等级
- 完整性等级越高，可靠性越高
- <u>高</u>等级数据**精确性**与**可靠性**><u>低</u>等级数据

##### 3. 三种策略

###### 3.1 下限标记策略

- 主体下限标记策略
  1. 主体**S**可**写**客体**O**     <=>    S等级>O等级
  2. 主体**S**读取完客体**O**后 ，S完整新=**最小上界**（S读取前，O）
  3. 主体**S1**可执行主体**S2**   <=> S1等级>s2等级

- 客体下限标记策略
  1. 写操作后，O完整性=**最大下界**（S写前，O）

###### 3.2 环策略

- S可以**写**O  <=> S>O
- S1**执行**S2 <=> S2>S1
- S可**读**任何O

###### 3.3 严格完整性策略

- 完整性*-属性：主体S可以**写**客体O  <=> S等级>O等级
- 援引规则：       主体S1可以**执行**主体S2   <=> S1等级>S2等级
- 简单完整性规则：主体S可以**读**客体O  <=>   S等级<O等级

