# 网站术语内容快照

快照日期：2026-09-10。共 35 个正式条目。

来源仓库：`energy-storage-product-reference/energy-dictionary-glossary`；每条记录保留来源文件与内容版本。已核对发布状态和同版本审阅记录，未宣称完成独立专业审查或逐项原始来源核验。

公开域名：未确认。配置与项目文档未提供公开站点地址；`sitePath` 是已对照本地构建产物检查的站内路由，不能当作完整网址。原始资料 URL 按网站记录保留，其可访问性和证据适配性须在使用时核查。

以下 JSON 是网站文本内容的原样字段快照（省略图示配置和来源展示数量）；UI 示意值不构成推荐设定或工程参数。`reviewRecord` 只代表网站个人审核与发布记录。按 ID 查找单条，无需通读全文。

<a id="term-utility-poc"></a>
## POC／并网连接点 · 大型储能

```json
{
  "id": "term-utility-poc",
  "sourceFile": "src/content/terms/utility-poc.md",
  "sitePath": "/terms/utility-scale-storage/poc/",
  "reviewRecord": {
    "termId": "term-utility-poc",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "已确认 POC 用于表达大型储能与公共电网的并网连接边界。"
    ]
  },
  "content": {
    "id": "term-utility-poc",
    "contentVersion": 1,
    "scene": "utility-scale-storage",
    "name": "POC／并网连接点",
    "english": "Point of Connection",
    "termType": "system",
    "category": "并网边界",
    "summary": "说明独立储能与公共电网交换功率、采集结果的连接边界。",
    "definition": "POC（Point of Connection，并网连接点）是储能电站与公共电网发生功率交换、计量和运行反馈的边界参照点。",
    "explanation": {
      "title": "通俗解释",
      "copy": "POC 就像储能电站接入公共电网的“门口”：电能从这里进出，功率和运行结果也通常围绕这里观察。"
    },
    "systemContent": {
      "responsibilities": [
        "POC 连接公共电网与独立储能电站。",
        "POC 是功率交换和测量结果的参照边界。",
        "调度、运行核对和结算口径可能使用 POC 相关数据。"
      ],
      "dataDimensions": [
        {
          "name": "交换功率",
          "description": "反映储能电站当前从电网吸收或向电网释放的功率。"
        },
        {
          "name": "计量结果",
          "description": "反映边界处记录的功率、电量或运行数据。"
        },
        {
          "name": "并网条件",
          "description": "反映系统能够交换多少功率以及是否允许当前动作。"
        }
      ],
      "scenarios": [
        {
          "name": "并网运行",
          "description": "储能电站通过 POC 与公共电网保持连接。"
        },
        {
          "name": "服务反馈",
          "description": "储能的功率响应和运行结果通过边界数据进行核对。"
        }
      ],
      "topologyBindings": [
        {
          "sceneId": "scene-utility-scale-storage",
          "topologyId": "utility-poc-relations",
          "isPrimary": true,
          "verificationStatus": "unverified",
          "evidenceRefs": [
            "phase-four-scope"
          ]
        }
      ]
    },
    "boundary": {
      "coreTitle": "边界口径",
      "coreCopy": "POC 是功能和计量上的并网连接点，页面不替代具体项目的一次接线、保护配置或并网协议。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "PCC／并网点",
          "description": "不同项目或资料可能使用 PCC、POI 等近似术语，具体名称和边界要以项目口径为准。"
        },
        {
          "term": "电网",
          "description": "电网是公共电力系统，POC 是储能与电网发生交换的边界参照。"
        },
        {
          "term": "PCS",
          "description": "PCS 负责电能转换，不等于储能接入公共电网的边界。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "看懂电站和公共电网之间的功率交换从哪里观察。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注并网边界、测量口径和系统配置之间的对应关系。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "把连接点、设备和运行结果分成不同层级表达。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "独立储能",
        "icon": "battery",
        "href": "/terms/utility-scale-storage/independent-storage/"
      },
      {
        "name": "AGC／自动发电控制",
        "icon": "gauge",
        "href": "/terms/utility-scale-storage/agc/"
      },
      {
        "name": "电力现货市场",
        "icon": "gauge",
        "href": "/terms/utility-scale-storage/spot-market/"
      },
      {
        "name": "PCS／储能变流器",
        "icon": "chip"
      }
    ],
    "sources": [
      {
        "label": "U.S. Department of Energy",
        "title": "Grid Energy Storage",
        "href": "https://www.energy.gov/oe/downloads/grid-energy-storage-December-2013"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "大型储能"
}
```

<a id="term-utility-spot-market"></a>
## 电力现货市场 · 大型储能

```json
{
  "id": "term-utility-spot-market",
  "sourceFile": "src/content/terms/utility-spot-market.md",
  "sitePath": "/terms/utility-scale-storage/spot-market/",
  "reviewRecord": {
    "termId": "term-utility-spot-market",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "已确认电力现货市场仅表达通用机制，不绑定地区交易规则。"
    ]
  },
  "content": {
    "id": "term-utility-spot-market",
    "contentVersion": 1,
    "scene": "utility-scale-storage",
    "name": "电力现货市场",
    "english": "Electricity Spot Market",
    "termType": "strategy",
    "category": "电力市场",
    "summary": "说明储能如何根据时段价格、申报和出清结果安排运行。",
    "definition": "电力现货市场是按较短时间尺度组织电能交易和出清的市场机制，储能可能依据适用规则参与申报、接受出清结果并执行充放电。",
    "explanation": {
      "title": "通俗解释",
      "copy": "电力现货市场可以理解成按时段确定电力供需和价格的交易机制：储能根据规则申报，按出清或调度结果安排充电、放电或待机。"
    },
    "boundary": {
      "coreTitle": "市场边界",
      "coreCopy": "页面只说明市场机制与储能运行的关系，不绑定具体地区的价格、准入、申报或收益规则。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "电网调峰",
          "description": "电网调峰是运行目标，现货市场是组织电能交易和出清的市场机制。"
        },
        {
          "term": "容量租赁",
          "description": "容量租赁围绕可用容量或服务能力安排，现货市场主要围绕时段电能交易。"
        },
        {
          "term": "AGC／自动发电控制",
          "description": "AGC 是运行控制过程，可能与市场安排有关，但不等于现货市场。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "看懂市场价格或出清结果为什么会影响储能运行安排。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注申报能力、SOC、PCS、并网点计量和执行边界。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分市场信号、运行调度、设备执行和计量反馈。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "独立储能",
        "icon": "battery",
        "href": "/terms/utility-scale-storage/independent-storage/"
      },
      {
        "name": "容量租赁",
        "icon": "battery",
        "href": "/terms/utility-scale-storage/capacity-lease/"
      },
      {
        "name": "AGC／自动发电控制",
        "icon": "gauge",
        "href": "/terms/utility-scale-storage/agc/"
      },
      {
        "name": "POC／并网连接点",
        "icon": "chip",
        "href": "/terms/utility-scale-storage/poc/"
      }
    ],
    "sources": [
      {
        "label": "国家能源局",
        "title": "关于加快推动新型储能发展的指导意见",
        "href": "https://www.nea.gov.cn/139896047_16189891532151n.pdf"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "大型储能"
}
```

<a id="term-utility-agc"></a>
## AGC／自动发电控制 · 大型储能

```json
{
  "id": "term-utility-agc",
  "sourceFile": "src/content/terms/utility-agc.md",
  "sitePath": "/terms/utility-scale-storage/agc/",
  "reviewRecord": {
    "termId": "term-utility-agc",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "已确认 AGC 表达调度控制过程，不绑定地区市场规则。"
    ]
  },
  "content": {
    "id": "term-utility-agc",
    "contentVersion": 1,
    "scene": "utility-scale-storage",
    "name": "AGC／自动发电控制",
    "english": "Automatic Generation Control",
    "termType": "strategy",
    "category": "调度与辅助服务",
    "summary": "通过自动功率控制信号，让储能按调度要求持续调整出力。",
    "definition": "AGC（Automatic Generation Control，自动发电控制）是一类自动功率控制过程，储能根据调度侧信号在允许范围内跟踪调整并网功率。",
    "explanation": {
      "title": "通俗解释",
      "copy": "AGC 可以理解成电网调度发给储能的一条“实时调节指令”：储能根据指令增加、减少或保持出力，并把实际结果反馈回去。"
    },
    "boundary": {
      "coreTitle": "控制边界",
      "coreCopy": "AGC 讲的是自动功率控制过程，不等于某个地区固定的市场产品，也不保证所有储能都能参与。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "一次调频",
          "description": "一次调频更关注频率变化后的快速响应，AGC 更强调跟随调度信号的自动调整。"
        },
        {
          "term": "EMS／能量管理系统",
          "description": "EMS 或站控系统可能负责接收、分解和执行 AGC 要求，AGC 不是 EMS 本身。"
        },
        {
          "term": "电力现货市场",
          "description": "现货市场是交易和出清机制，AGC 是运行控制过程。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解储能为什么需要按外部调度信号持续改变功率。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注信号、响应速度、SOC、PCS 能力和并网条件。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分调度信号、站控执行和最终功率反馈。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "一次调频",
        "icon": "gauge",
        "href": "/terms/utility-scale-storage/primary-frequency-regulation/"
      },
      {
        "name": "独立储能",
        "icon": "battery",
        "href": "/terms/utility-scale-storage/independent-storage/"
      },
      {
        "name": "POC／并网连接点",
        "icon": "chip",
        "href": "/terms/utility-scale-storage/poc/"
      },
      {
        "name": "EMS／能量管理系统",
        "icon": "chip"
      }
    ],
    "sources": [
      {
        "label": "U.S. Department of Energy",
        "title": "Energy Storage in Ancillary Service Applications",
        "href": "https://www.energy.gov/sites/default/files/2013/11/f5/51294.pdf"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "大型储能"
}
```

<a id="term-utility-primary-frequency-regulation"></a>
## 一次调频 · 大型储能

```json
{
  "id": "term-utility-primary-frequency-regulation",
  "sourceFile": "src/content/terms/utility-primary-frequency-regulation.md",
  "sitePath": "/terms/utility-scale-storage/primary-frequency-regulation/",
  "reviewRecord": {
    "termId": "term-utility-primary-frequency-regulation",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "已确认一次调频表达电网支撑能力，保留设备与适用规则边界。"
    ]
  },
  "content": {
    "id": "term-utility-primary-frequency-regulation",
    "contentVersion": 1,
    "scene": "utility-scale-storage",
    "name": "一次调频",
    "english": "Primary Frequency Regulation",
    "termType": "strategy",
    "category": "调度与辅助服务",
    "summary": "电网频率变化时，储能依据响应规则快速改变功率。",
    "definition": "一次调频是电网频率发生偏差后，资源依据预设响应关系自主或快速改变有功功率，以帮助抑制频率偏差的电网支撑过程。",
    "explanation": {
      "title": "通俗解释",
      "copy": "一次调频像电网频率变化时的“快速反应”：频率偏离后，储能按预设关系及时增加或减少功率，先帮助稳住变化。"
    },
    "boundary": {
      "coreTitle": "响应边界",
      "coreCopy": "一次调频描述频率变化后的响应能力，是否启用、响应范围和考核方式取决于设备能力与适用规则。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "AGC／自动发电控制",
          "description": "AGC 主要跟随调度信号调整功率，一次调频主要由频率变化触发快速响应。"
        },
        {
          "term": "惯量支撑",
          "description": "惯量支撑关注更早阶段的频率变化响应，不能与一次调频简单画等号。"
        },
        {
          "term": "PCS",
          "description": "PCS 是执行功率转换的设备，不等于一次调频服务本身。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "看懂频率变化为什么会触发储能快速改变出力。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注响应曲线、测量频率、功率边界和电池状态。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "把电网状态、响应规则和设备执行分别表达。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "AGC／自动发电控制",
        "icon": "gauge",
        "href": "/terms/utility-scale-storage/agc/"
      },
      {
        "name": "独立储能",
        "icon": "battery",
        "href": "/terms/utility-scale-storage/independent-storage/"
      },
      {
        "name": "惯量支撑",
        "icon": "gauge"
      },
      {
        "name": "POC／并网连接点",
        "icon": "chip",
        "href": "/terms/utility-scale-storage/poc/"
      }
    ],
    "sources": [
      {
        "label": "U.S. Department of Energy",
        "title": "Energy Storage in Ancillary Service Applications",
        "href": "https://www.energy.gov/sites/default/files/2013/11/f5/51294.pdf"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "大型储能"
}
```

<a id="term-commercial-pcs"></a>
## PCS／储能变流器 · 工商业储能

```json
{
  "id": "term-commercial-pcs",
  "sourceFile": "src/content/terms/commercial-pcs.md",
  "sitePath": "/terms/commercial/pcs/",
  "reviewRecord": {
    "termId": "term-commercial-pcs",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "PCS 只表达双向变流功能，不推断具体工程设备组合。"
    ]
  },
  "content": {
    "id": "term-commercial-pcs",
    "contentVersion": 1,
    "scene": "commercial-storage",
    "name": "PCS／储能变流器",
    "english": "Power Conversion System",
    "termType": "device",
    "category": "工商业储能",
    "summary": "理解 PCS 如何完成储能电池与工商业交流侧之间的双向电能转换。",
    "definition": "PCS 在储能电池直流侧与工商业交流侧之间进行双向电能转换。",
    "explanation": {
      "title": "通俗解释",
      "copy": "在工商业储能里，PCS 仍是一台双向“变电转换器”：负责电池直流电和场站交流电之间互相转换，按 EMS 安排执行充放电。"
    },
    "boundary": {
      "coreTitle": "功能边界",
      "coreCopy": "PCS 执行电能转换，EMS 安排运行，BMS 提供电池状态与允许条件；实际功率和并网能力取决于系统配置。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "EMS／能量管理系统",
          "description": "EMS 根据负荷、目标和设备状态安排运行，PCS 按允许条件执行转换。"
        },
        {
          "term": "BMS／电池管理系统",
          "description": "BMS 管理电池状态和保护条件，不承担主动功率转换。"
        },
        {
          "term": "混合光储逆变器",
          "description": "户用混合光储逆变器常集成 PCS 功能；工商业场站的设备组合取决于系统配置。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "看懂储能为什么能在工商业交流侧充电或放电。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注直流侧、交流侧、并网点和电池允许条件之间的转换边界。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分 PCS 的变流功能、EMS 的调度作用和电池的储能作用。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "EMS／能量管理系统",
        "icon": "chip",
        "href": "/terms/commercial/ems/"
      },
      {
        "name": "BMS／电池管理系统",
        "icon": "chip",
        "href": "/terms/commercial/bms/"
      },
      {
        "name": "SOC／电池荷电状态",
        "icon": "gauge",
        "href": "/terms/commercial/soc/"
      },
      {
        "name": "混合光储逆变器",
        "icon": "battery",
        "href": "/terms/hybrid-inverter/"
      }
    ],
    "sources": [
      {
        "label": "NREL",
        "title": "Energy Storage Systems Integration",
        "href": "https://www.nrel.gov/docs/fy17osti/67463.pdf"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "工商业储能"
}
```

<a id="term-commercial-islanded-operation"></a>
## 孤岛运行 · 工商业储能

```json
{
  "id": "term-commercial-islanded-operation",
  "sourceFile": "src/content/terms/commercial-islanded-operation.md",
  "sitePath": "/terms/commercial/islanded-operation/",
  "reviewRecord": {
    "termId": "term-commercial-islanded-operation",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "孤岛运行表达断网隔离后的运行状态，不表达备电策略或固定接线。"
    ]
  },
  "content": {
    "id": "term-commercial-islanded-operation",
    "contentVersion": 1,
    "scene": "commercial-storage",
    "name": "孤岛运行",
    "english": "Islanded Operation",
    "aliases": [
      "Island Mode"
    ],
    "termType": "state",
    "category": "工商业储能",
    "summary": "理解工商业储能与公共电网隔离后如何在本地运行。",
    "definition": "工商业储能与公共电网断开并完成隔离后，由本地可用能源按配置给部分负载供电的运行状态。",
    "definitionNote": "Island Mode 是常见的英文表达。",
    "explanation": {
      "title": "通俗解释",
      "copy": "在工商业场站里，孤岛运行表示系统与公共电网隔离后，由本地可用的光伏、储能和其他电源按配置继续给部分负载供电。"
    },
    "boundary": {
      "coreTitle": "状态边界",
      "coreCopy": "孤岛运行是电网断开后的运行状态，不是需量控制或电量预留策略；进入前必须与公共电网隔离。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "备电模式",
          "description": "备电模式决定要保留多少电、优先供哪些负载；孤岛运行描述电网断开后的状态。"
        },
        {
          "term": "负载削峰",
          "description": "负载削峰是功率目标，不等于系统已经进入孤岛运行。"
        },
        {
          "term": "系统配置",
          "description": "可供电负载取决于逆变器能力、电池状态、隔离条件和场站配置。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解电网异常后系统为什么要隔离，以及哪些负载还能继续供电。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注隔离、并网恢复、负载范围和本地能源可用状态。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分运行状态、功率策略和设备能力，不把孤岛运行写成电量预留。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "EMS／能量管理系统",
        "icon": "chip",
        "href": "/terms/commercial/ems/"
      },
      {
        "name": "PCS／储能变流器",
        "icon": "chip",
        "href": "/terms/commercial/pcs/"
      },
      {
        "name": "SOC／电池荷电状态",
        "icon": "gauge",
        "href": "/terms/commercial/soc/"
      },
      {
        "name": "电池系统",
        "icon": "battery",
        "href": "/terms/battery-system/"
      }
    ],
    "sources": [
      {
        "label": "U.S. Department of Energy",
        "title": "Microgrid Systems",
        "href": "https://www.energy.gov/oe/microgrid-systems"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "工商业储能"
}
```

<a id="term-commercial-soc"></a>
## SOC／电池荷电状态 · 工商业储能

```json
{
  "id": "term-commercial-soc",
  "sourceFile": "src/content/terms/commercial-soc.md",
  "sitePath": "/terms/commercial/soc/",
  "reviewRecord": {
    "termId": "term-commercial-soc",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "SOC 作为当前荷电状态解释，不与 SOH、可用容量或功率混淆。"
    ]
  },
  "content": {
    "id": "term-commercial-soc",
    "contentVersion": 1,
    "scene": "commercial-storage",
    "name": "SOC／电池荷电状态",
    "english": "State of Charge",
    "termType": "state",
    "category": "工商业储能",
    "summary": "理解 SOC 如何表示工商业储能电池当前的荷电程度。",
    "definition": "SOC 表示工商业储能电池当前相对于参考满电容量的荷电程度，通常以百分比表示。",
    "explanation": {
      "title": "通俗解释",
      "copy": "在工商业储能里，SOC 是 EMS 安排削峰和分时充放电时要看的电量刻度：电池是否还有足够电量，会影响目标能否执行。"
    },
    "stateContent": {
      "defaultValue": 62,
      "chargeCopy": "充电时，SOC 通常向满电参考状态移动。",
      "dischargeCopy": "放电时，SOC 通常向低荷电参考状态移动；实际可用范围还受系统设定约束。"
    },
    "boundary": {
      "coreTitle": "状态边界",
      "coreCopy": "SOC 看当前荷电程度，不直接等同于可用容量、健康度或当前允许功率。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "SOH／电池健康度",
          "description": "SOH 描述相对于参考状态的健康程度，SOC 描述当前荷电位置。"
        },
        {
          "term": "BMS／电池管理系统",
          "description": "BMS 负责估算 SOC 并结合保护条件提供允许功率。"
        },
        {
          "term": "负载削峰",
          "description": "削峰能否执行取决于 SOC、可用功率和系统设定。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解为什么电池不会一直充满或放空，以及可用电量如何影响运行目标。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注 SOC 估算口径、运行上下限和电池系统保护条件。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "将 SOC 与 SOH、可用容量和允许功率明确区分。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "BMS／电池管理系统",
        "icon": "chip",
        "href": "/terms/commercial/bms/"
      },
      {
        "name": "EMS／能量管理系统",
        "icon": "chip",
        "href": "/terms/commercial/ems/"
      },
      {
        "name": "负载削峰",
        "icon": "gauge",
        "href": "/terms/commercial/peak-shaving/"
      },
      {
        "name": "峰谷套利",
        "icon": "gauge",
        "href": "/terms/commercial/peak-valley-arbitrage/"
      }
    ],
    "sources": [
      {
        "label": "U.S. Department of Energy",
        "title": "Energy Storage",
        "href": "https://www.energy.gov/oe/energy-storage"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "工商业储能"
}
```

<a id="term-commercial-demand-control"></a>
## 需量控制 · 工商业储能

```json
{
  "id": "term-commercial-demand-control",
  "sourceFile": "src/content/terms/commercial-demand-control.md",
  "sitePath": "/terms/commercial/demand-control/",
  "reviewRecord": {
    "termId": "term-commercial-demand-control",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "需量控制聚焦计量点目标上限，具体规则留给项目配置和适用政策。"
    ]
  },
  "content": {
    "id": "term-commercial-demand-control",
    "contentVersion": 1,
    "scene": "commercial-storage",
    "name": "需量控制",
    "english": "Demand Control",
    "termType": "strategy",
    "category": "工商业储能",
    "summary": "理解如何控制工商业场站计量点的最大用电功率。",
    "definition": "通过储能和运行安排，控制工商业场站在计量点的最大用电功率。",
    "explanation": {
      "title": "通俗解释",
      "copy": "需量控制关注“这一刻从电网取了多大功率”：负荷接近上限时，电池补一部分电，帮助压低计量点峰值。"
    },
    "boundary": {
      "coreTitle": "功率目标",
      "coreCopy": "需量控制关注计量点的最大用电功率，不等于减少总用电量，也不等于峰谷电价套利。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "负载削峰",
          "description": "负载削峰关注压低电网侧瞬时功率峰值；需量控制强调计量点的目标上限。"
        },
        {
          "term": "峰谷套利",
          "description": "峰谷套利关注电价时段，不是计量点功率上限。"
        },
        {
          "term": "SOC／电池荷电状态",
          "description": "能否维持需量目标取决于电池 SOC、可用功率和系统设定。"
        },
        {
          "term": "目标规则",
          "description": "具体需量计费规则和上限以适用地区政策及项目配置为准。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解为什么负荷接近上限时，储能会补电，压低计量点峰值。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注计量点、目标上限、响应功率和电池可用状态。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分需量目标、负载削峰和峰谷电价策略，不做收益承诺。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "负载削峰",
        "icon": "gauge",
        "href": "/terms/commercial/peak-shaving/"
      },
      {
        "name": "峰谷套利",
        "icon": "gauge",
        "href": "/terms/commercial/peak-valley-arbitrage/"
      },
      {
        "name": "EMS／能量管理系统",
        "icon": "chip",
        "href": "/terms/commercial/ems/"
      },
      {
        "name": "SOC／电池荷电状态",
        "icon": "gauge",
        "href": "/terms/commercial/soc/"
      }
    ],
    "sources": [
      {
        "label": "SMA",
        "title": "Peak Load Shaving Function",
        "href": "https://manuals.sma.de/SBSxx-US-10/en-US/391139595.html"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "工商业储能"
}
```

<a id="term-commercial-peak-shaving"></a>
## 负载削峰 · 工商业储能

```json
{
  "id": "term-commercial-peak-shaving",
  "sourceFile": "src/content/terms/commercial-peak-shaving.md",
  "sitePath": "/terms/commercial/peak-shaving/",
  "reviewRecord": {
    "termId": "term-commercial-peak-shaving",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "负载削峰聚焦计量点功率峰值，不承诺降低总用电量。"
    ]
  },
  "content": {
    "id": "term-commercial-peak-shaving",
    "contentVersion": 1,
    "scene": "commercial-storage",
    "name": "负载削峰",
    "english": "Peak Shaving",
    "termType": "strategy",
    "category": "工商业储能",
    "summary": "理解如何用储能压低工商业场站的电网侧瞬时功率峰值。",
    "definition": "通过储能补电，压低工商业场站某一时刻从电网取电的最大功率。",
    "explanation": {
      "title": "通俗解释",
      "copy": "当工商业负荷突然升高时，电池补一部分电，让计量点功率尽量不超过设定的需量或功率目标。"
    },
    "boundary": {
      "coreTitle": "功率目标",
      "coreCopy": "负载削峰关注计量点功率峰值，重点是压低电网侧瞬时功率，不等于减少总用电量。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "需量控制",
          "description": "需量控制同样关注计量点功率上限，具体目标和计费口径以系统设定及适用规则为准。"
        },
        {
          "term": "峰谷套利",
          "description": "峰谷套利看电价时段安排充放电，重点不是瞬时功率上限。"
        },
        {
          "term": "SOC／电池荷电状态",
          "description": "电池要有足够 SOC 和放电功率，才能补上瞬时负荷。"
        },
        {
          "term": "自发自用",
          "description": "自发自用优先消纳光伏电量；削峰的触发依据是电网侧功率目标。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解为什么负荷同时升高时电池会补电，以及电网侧峰值如何降低。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注计量点功率上限、电池可用功率和设备响应条件。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分功率目标、电价目标和自发自用目标，不把削峰写成减少总用电量。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "需量控制",
        "icon": "gauge",
        "href": "/terms/commercial/demand-control/"
      },
      {
        "name": "峰谷套利",
        "icon": "gauge",
        "href": "/terms/commercial/peak-valley-arbitrage/"
      },
      {
        "name": "SOC／电池荷电状态",
        "icon": "gauge",
        "href": "/terms/commercial/soc/"
      },
      {
        "name": "EMS／能量管理系统",
        "icon": "chip",
        "href": "/terms/commercial/ems/"
      }
    ],
    "sources": [
      {
        "label": "SMA",
        "title": "Peak Load Shaving Function",
        "href": "https://manuals.sma.de/SBSxx-US-10/en-US/391139595.html"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "工商业储能"
}
```

<a id="term-commercial-peak-valley-arbitrage"></a>
## 峰谷套利 · 工商业储能

```json
{
  "id": "term-commercial-peak-valley-arbitrage",
  "sourceFile": "src/content/terms/commercial-peak-valley-arbitrage.md",
  "sitePath": "/terms/commercial/peak-valley-arbitrage/",
  "reviewRecord": {
    "termId": "term-commercial-peak-valley-arbitrage",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "峰谷套利只解释时段价差机制，不绑定地区电价或收益。"
    ]
  },
  "content": {
    "id": "term-commercial-peak-valley-arbitrage",
    "contentVersion": 1,
    "scene": "commercial-storage",
    "name": "峰谷套利",
    "english": "Peak-valley Arbitrage",
    "termType": "strategy",
    "category": "工商业储能",
    "summary": "理解如何按工商业峰谷电价时段安排储能充放电。",
    "definition": "低电价时充电，高电价时放电，利用适用的时段价差减少购电成本。",
    "explanation": {
      "title": "通俗解释",
      "copy": "工商业峰谷套利按适用的电价时段安排充放电：低价时存电，高价时使用；实际节省还要看电价差、损耗和可用电量。"
    },
    "boundary": {
      "coreTitle": "电价目标",
      "coreCopy": "峰谷套利关注电价和时间，需要适用的峰谷电价与允许的充放电策略，不承诺固定收益。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "负载削峰",
          "description": "负载削峰看计量点功率峰值；峰谷套利看电价时段。"
        },
        {
          "term": "需量控制",
          "description": "需量控制关注计量点功率上限，不等同于利用峰谷价差。"
        },
        {
          "term": "SOC／电池荷电状态",
          "description": "可用电量和 SOC 会限制低价充电、高价放电的实际执行范围。"
        },
        {
          "term": "自发自用",
          "description": "自发自用优先消纳光伏电量；能否与峰谷套利叠加及优先级以系统设定为准。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解为什么系统会在低价时段充电、高价时段放电，以及节省会受哪些条件影响。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注峰谷时段、电价差、充放电损耗和电池可用电量。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分电价策略、功率策略和自发自用策略，不绑定具体地区电价或收益承诺。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "负载削峰",
        "icon": "gauge",
        "href": "/terms/commercial/peak-shaving/"
      },
      {
        "name": "需量控制",
        "icon": "gauge",
        "href": "/terms/commercial/demand-control/"
      },
      {
        "name": "SOC／电池荷电状态",
        "icon": "gauge",
        "href": "/terms/commercial/soc/"
      },
      {
        "name": "EMS／能量管理系统",
        "icon": "chip",
        "href": "/terms/commercial/ems/"
      }
    ],
    "sources": [
      {
        "label": "U.S. Department of Energy",
        "title": "Energy Storage Valuation",
        "href": "https://www.energy.gov/sites/default/files/2022-06/MSP_Report_2022June_Final_508_v3.pdf"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "工商业储能"
}
```

<a id="term-commercial-bms"></a>
## BMS／电池管理系统 · 工商业储能

```json
{
  "id": "term-commercial-bms",
  "sourceFile": "src/content/terms/commercial-bms.md",
  "sitePath": "/terms/commercial/bms/",
  "reviewRecord": {
    "termId": "term-commercial-bms",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "保留 BMS 的状态、保护和允许功率边界，不扩展设备参数。"
    ]
  },
  "content": {
    "id": "term-commercial-bms",
    "contentVersion": 1,
    "scene": "commercial-storage",
    "name": "BMS／电池管理系统",
    "english": "Battery Management System",
    "termType": "system",
    "category": "工商业储能",
    "summary": "理解 BMS 如何为工商业储能提供电池状态、保护和充放电允许条件。",
    "definition": "BMS 监测工商业储能电池状态，并根据保护条件管理充放电允许范围的系统。",
    "explanation": {
      "title": "通俗解释",
      "copy": "在工商业储能里，BMS 仍是电池的“安全管家”：它把电池状态和允许条件提供给 EMS、PCS，支持大功率设备的安全运行。"
    },
    "systemContent": {
      "responsibilities": [
        "采集电池簇或电池包的电压、电流、温度等运行信息。",
        "估算 SOC、SOH 等状态，为充放电控制提供依据。",
        "根据保护条件限制或停止充放电，管理异常和告警状态。",
        "向 PCS、EMS 提供状态、告警和允许功率。"
      ],
      "dataDimensions": [
        {
          "name": "电池状态",
          "description": "反映电压、电流、温度、SOC 和 SOH 等状态信息。"
        },
        {
          "name": "保护与告警",
          "description": "反映异常状态以及当前是否允许继续充放电。"
        },
        {
          "name": "允许功率边界",
          "description": "反映受状态和保护条件约束的充放电功率范围。"
        }
      ],
      "scenarios": [
        {
          "name": "运行保护",
          "description": "在削峰、套利等运行目标下持续提供电池侧保护条件。"
        },
        {
          "name": "状态反馈",
          "description": "向 EMS 和 PCS 提供电池状态与允许功率，支持设备协同运行。"
        }
      ],
      "topologyBindings": [
        {
          "sceneId": "scene-commercial-storage",
          "topologyId": "commercial-storage-relations",
          "isPrimary": true,
          "verificationStatus": "verified",
          "evidenceRefs": [
            "commercial-storage-preview"
          ]
        }
      ]
    },
    "boundary": {
      "coreTitle": "系统边界",
      "coreCopy": "BMS 负责电池侧监测、估算、保护和允许条件，不负责制定站点级功率或电价目标，也不承担主动功率转换。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "EMS／能量管理系统",
          "description": "EMS 负责站点级运行安排，BMS 负责电池状态和保护条件。"
        },
        {
          "term": "PCS／储能变流器",
          "description": "PCS 负责功率转换，BMS 提供电池状态和允许功率。"
        },
        {
          "term": "SOC／电池荷电状态",
          "description": "SOC 是 BMS 估算和提供的一项电池状态，不等于完整的电池管理功能。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "看懂 SOC、SOH、告警和充放电允许状态如何影响储能可用性。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注电池簇状态、保护条件、通信和充放电联锁边界。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分测量、估算、保护、告警和允许功率，不把 BMS 写成电池或 PCS。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "EMS／能量管理系统",
        "icon": "chip",
        "href": "/terms/commercial/ems/"
      },
      {
        "name": "PCS／储能变流器",
        "icon": "chip",
        "href": "/terms/commercial/pcs/"
      },
      {
        "name": "SOC／电池荷电状态",
        "icon": "gauge",
        "href": "/terms/commercial/soc/"
      },
      {
        "name": "电池系统",
        "icon": "battery",
        "href": "/terms/battery-system/"
      }
    ],
    "sources": [
      {
        "label": "U.S. Department of Energy",
        "title": "Energy Storage",
        "href": "https://www.energy.gov/oe/energy-storage"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "工商业储能"
}
```

<a id="term-commercial-ems"></a>
## EMS／能量管理系统 · 工商业储能

```json
{
  "id": "term-commercial-ems",
  "sourceFile": "src/content/terms/commercial-ems.md",
  "sitePath": "/terms/commercial/ems/",
  "reviewRecord": {
    "termId": "term-commercial-ems",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "工商业语境与户用 EMS 页面分开表达，保留通用调度边界。"
    ]
  },
  "content": {
    "id": "term-commercial-ems",
    "contentVersion": 1,
    "scene": "commercial-storage",
    "name": "EMS／能量管理系统",
    "english": "Energy Management System",
    "termType": "system",
    "category": "工商业储能",
    "summary": "理解 EMS 如何结合负荷、电价和设备状态安排工商业储能运行。",
    "definition": "EMS 根据负荷、运行目标、电价时段和设备状态，在设备允许条件下协调工商业储能运行。",
    "explanation": {
      "title": "通俗解释",
      "copy": "EMS 是工商业储能的“调度大脑”：它结合负荷、需量目标、电价时段和电池状态，安排什么时候充电、什么时候放电。"
    },
    "systemContent": {
      "responsibilities": [
        "EMS 接收负荷、电价和运行目标信息并安排运行。",
        "PCS 执行电能转换，并反馈运行情况。",
        "BMS 为 EMS 和 PCS 提供电池状态与充放电允许条件。"
      ],
      "dataDimensions": [
        {
          "name": "负荷与并网点功率",
          "description": "反映工商业负荷和计量点当前的用电功率。"
        },
        {
          "name": "电价与运行目标",
          "description": "反映需量控制、峰谷套利等目标及适用的时段条件。"
        },
        {
          "name": "电池状态与允许条件",
          "description": "反映 SOC、功率边界和保护条件，决定当前能否充放电。"
        }
      ],
      "scenarios": [
        {
          "name": "负载削峰",
          "description": "EMS 根据功率上限安排电池在负荷峰值时补电。"
        },
        {
          "name": "峰谷套利",
          "description": "EMS 根据电价时段安排低价充电和高价放电。"
        }
      ],
      "topologyBindings": [
        {
          "sceneId": "scene-commercial-storage",
          "topologyId": "commercial-storage-relations",
          "isPrimary": true,
          "verificationStatus": "verified",
          "evidenceRefs": [
            "commercial-storage-preview"
          ]
        }
      ]
    },
    "boundary": {
      "coreTitle": "系统边界",
      "coreCopy": "EMS 负责结合信息和目标安排运行，实际执行仍受 PCS 能力、电池状态、并网点和系统配置约束。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "PCS／储能变流器",
          "description": "PCS 执行电池直流电与场站交流电之间的转换；EMS 负责运行安排。"
        },
        {
          "term": "BMS／电池管理系统",
          "description": "BMS 提供电池状态、保护和充放电允许条件；EMS 不替代电池管理。"
        },
        {
          "term": "需量控制",
          "description": "需量控制是功率目标，EMS 可以在设备允许条件下安排执行。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "看懂为什么负荷变化或电价变化时，储能会安排充电或放电。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注计量点、设备能力、电池允许条件和运行目标之间的配合。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分运行目标、调度安排和 PCS 的实际执行反馈。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "PCS／储能变流器",
        "icon": "chip",
        "href": "/terms/commercial/pcs/"
      },
      {
        "name": "BMS／电池管理系统",
        "icon": "chip",
        "href": "/terms/commercial/bms/"
      },
      {
        "name": "SOC／电池荷电状态",
        "icon": "gauge",
        "href": "/terms/commercial/soc/"
      },
      {
        "name": "负载削峰",
        "icon": "gauge",
        "href": "/terms/commercial/peak-shaving/"
      }
    ],
    "sources": [
      {
        "label": "SMA",
        "title": "Energy Management Overview",
        "href": "https://www.sma.de/en/products/energy-management/sunny-home-manager"
      },
      {
        "label": "U.S. Department of Energy",
        "title": "Energy Storage",
        "href": "https://www.energy.gov/oe/energy-storage"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "工商业储能"
}
```

<a id="term-solar-charging-charging-station-demand-control"></a>
## 充电站需量控制 · 光储充一体化

```json
{
  "id": "term-solar-charging-charging-station-demand-control",
  "sourceFile": "src/content/terms/solar-charging-charging-station-demand-control.md",
  "sitePath": "/terms/solar-storage-charging/charging-station-demand-control/",
  "reviewRecord": {
    "termId": "term-solar-charging-charging-station-demand-control",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "光储充正式内容，新增充电站并网点需量控制关系，已完成产品确认。"
    ]
  },
  "content": {
    "id": "term-solar-charging-charging-station-demand-control",
    "contentVersion": 1,
    "scene": "solar-storage-charging",
    "name": "充电站需量控制",
    "english": "EV Charging Station Demand Control",
    "termType": "strategy",
    "category": "功能与策略",
    "summary": "理解如何控制园区或充电场站并网点的最大取电功率。",
    "definition": "充电站需量控制是通过储能和充电安排，控制充电场站在并网点的最大取电功率的运行策略。",
    "explanation": {
      "title": "通俗解释",
      "copy": "当很多车辆同时充电时，储能可以补一部分电，或者把充电安排得更分散，让充电站从电网取电的功率峰值不超过设定目标。"
    },
    "aliases": [
      "需量控制"
    ],
    "boundary": {
      "coreTitle": "功率目标",
      "coreCopy": "充电站需量控制关注并网点的最大取电功率，不等于减少总充电量，也不绑定具体地区的计费口径。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "自发自用",
          "description": "自发自用看光伏电能是否在场站本地被消纳；需量控制看并网点功率峰值。"
        },
        {
          "term": "有序充电",
          "description": "有序充电通过调整充电时段或功率帮助执行安排，需量控制是要控制的并网点功率目标。"
        },
        {
          "term": "功率分配",
          "description": "功率分配决定各对象当前分到多少功率，但不等于需量目标本身。"
        },
        {
          "term": "运行条件",
          "description": "能否维持目标取决于储能可用功率、SOC、充电需求和系统配置。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解车辆集中充电时，为什么储能会补电或调整充电安排。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注并网点、需量目标、储能可用功率和充电负载边界。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分光伏消纳、需量目标和充电安排，不把功率峰值控制写成减少总用电量。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "自发自用",
        "icon": "home",
        "href": "/terms/solar-storage-charging/self-consumption/"
      },
      {
        "name": "有序充电",
        "icon": "gauge",
        "href": "/terms/solar-storage-charging/managed-charging/"
      },
      {
        "name": "功率分配",
        "icon": "gauge",
        "href": "/terms/solar-storage-charging/power-allocation/"
      },
      {
        "name": "EMS／能量管理系统",
        "icon": "chip",
        "href": "/terms/solar-storage-charging/ems/"
      }
    ],
    "sources": [
      {
        "label": "U.S. Department of Energy",
        "title": "Energy Storage",
        "href": "https://www.energy.gov/oe/energy-storage"
      },
      {
        "label": "U.S. Department of Energy",
        "title": "Electric Vehicle Charging",
        "href": "https://www.energy.gov/energysaver/electric-vehicles"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "光储充一体化"
}
```

<a id="term-solar-charging-managed-charging"></a>
## 有序充电 · 光储充一体化

```json
{
  "id": "term-solar-charging-managed-charging",
  "sourceFile": "src/content/terms/solar-charging-managed-charging.md",
  "sitePath": "/terms/solar-storage-charging/managed-charging/",
  "reviewRecord": {
    "termId": "term-solar-charging-managed-charging",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "光储充正式内容，已确认术语边界、图示关系和参考来源。"
    ]
  },
  "content": {
    "id": "term-solar-charging-managed-charging",
    "contentVersion": 1,
    "scene": "solar-storage-charging",
    "name": "有序充电",
    "english": "Managed Charging",
    "termType": "strategy",
    "category": "功能与策略",
    "summary": "根据场站充电需求、可用功率和运行目标安排充电时段或功率的策略。",
    "definition": "有序充电是一类场站充电调度策略，通过调整充电开始时间或充电功率，使充电需求与可用电能和系统边界相协调。",
    "explanation": {
      "title": "通俗解释",
      "copy": "有序充电不是不让车充电，而是“把场站充电安排得更合适”：功率紧张时少一点或晚一点，条件合适时再多充一些。"
    },
    "boundary": {
      "coreTitle": "系统边界",
      "coreCopy": "本页不涉及车网互动、充电运营或地区性电价规则。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "功率分配",
          "description": "功率分配关注各对象当前分到多少功率；有序充电关注充电何时、以什么功率执行。"
        },
        {
          "term": "充电设施",
          "description": "充电设施是执行端，有序充电是运行策略。"
        },
        {
          "term": "充电完成时间",
          "description": "具体完成时间取决于需求、可用功率和系统设定。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解充电开始时间或功率为什么可能变化。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注充电负载、供电能力和系统边界。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "明确计划、实际功率和完成状态不能混为一谈。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "EMS／能量管理系统",
        "icon": "chip",
        "href": "/terms/solar-storage-charging/ems/"
      },
      {
        "name": "充电设施",
        "icon": "chip",
        "href": "/terms/solar-storage-charging/ev-charging-infrastructure/"
      },
      {
        "name": "功率分配",
        "icon": "gauge",
        "href": "/terms/solar-storage-charging/power-allocation/"
      }
    ],
    "sources": [
      {
        "label": "U.S. Department of Energy",
        "title": "Electric Vehicle Charging",
        "href": "https://www.energy.gov/energysaver/electric-vehicles"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "光储充一体化"
}
```

<a id="term-solar-charging-power-allocation"></a>
## 功率分配 · 光储充一体化

```json
{
  "id": "term-solar-charging-power-allocation",
  "sourceFile": "src/content/terms/solar-charging-power-allocation.md",
  "sitePath": "/terms/solar-storage-charging/power-allocation/",
  "reviewRecord": {
    "termId": "term-solar-charging-power-allocation",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "光储充正式内容，已确认术语边界、图示关系和参考来源。"
    ]
  },
  "content": {
    "id": "term-solar-charging-power-allocation",
    "contentVersion": 1,
    "scene": "solar-storage-charging",
    "name": "功率分配",
    "english": "Power Allocation",
    "termType": "strategy",
    "category": "功能与策略",
    "summary": "在光伏、储能、电网和场站充电需求之间安排当前可用功率的策略。",
    "definition": "功率分配是根据可用电能、储能状态、并网点边界和充电需求，在多个供电对象之间安排当前功率的运行过程。",
    "explanation": {
      "title": "通俗解释",
      "copy": "功率分配就是回答“现在这部分电给谁用”：EMS 会结合光伏、电网、储能、并网点和充电需求安排当前功率去向。"
    },
    "boundary": {
      "coreTitle": "系统边界",
      "coreCopy": "本页表达通用功率协调关系，不规定具体系统的优先级或控制算法。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "有序充电",
          "description": "有序充电关注充电时段和功率安排，功率分配关注多个对象之间的当前去向。"
        },
        {
          "term": "自发自用",
          "description": "是否优先使用光伏、储能或电网取决于系统策略，不能预设唯一顺序。"
        },
        {
          "term": "功率上限",
          "description": "功率分配受设备能力、并网边界和当前状态约束。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解同一时刻的电能为什么会在不同对象之间变化。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注供电来源、储能状态和充电负载边界。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "同时表达来源、去向、计划功率和实际功率。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "EMS／能量管理系统",
        "icon": "chip",
        "href": "/terms/solar-storage-charging/ems/"
      },
      {
        "name": "储能系统",
        "icon": "battery",
        "href": "/terms/solar-storage-charging/energy-storage-system/"
      },
      {
        "name": "有序充电",
        "icon": "gauge",
        "href": "/terms/solar-storage-charging/managed-charging/"
      },
      {
        "name": "充电设施",
        "icon": "chip",
        "href": "/terms/solar-storage-charging/ev-charging-infrastructure/"
      }
    ],
    "sources": [
      {
        "label": "U.S. Department of Energy",
        "title": "Energy Storage",
        "href": "https://www.energy.gov/oe/energy-storage"
      },
      {
        "label": "U.S. Department of Energy",
        "title": "Electric Vehicle Charging",
        "href": "https://www.energy.gov/energysaver/electric-vehicles"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "光储充一体化"
}
```

<a id="term-solar-charging-self-consumption"></a>
## 自发自用 · 光储充一体化

```json
{
  "id": "term-solar-charging-self-consumption",
  "sourceFile": "src/content/terms/solar-charging-self-consumption.md",
  "sitePath": "/terms/solar-storage-charging/self-consumption/",
  "reviewRecord": {
    "termId": "term-solar-charging-self-consumption",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "光储充正式内容，新增场站语境下的光伏自发自用与就地消纳关系，已完成产品确认。"
    ]
  },
  "content": {
    "id": "term-solar-charging-self-consumption",
    "contentVersion": 1,
    "scene": "solar-storage-charging",
    "name": "自发自用",
    "english": "Self-consumption",
    "termType": "strategy",
    "category": "功能与策略",
    "summary": "理解光伏电能如何在园区或充电场站本地供给充电负载。",
    "definition": "自发自用是指光伏发电在用户侧本地被消纳，既可以直接供给充电负载，也可以先存入储能系统、在后续时段再供给充电负载。",
    "explanation": {
      "title": "通俗解释",
      "copy": "自发自用就是让光伏发的电尽量在场站本地使用：有充电需求时优先供给充电负载，用不完的部分再存进电池，之后继续供给充电负载。"
    },
    "aliases": [
      "光伏就地消纳",
      "就地消纳"
    ],
    "strategyContent": {
      "scenarios": [
        {
          "id": "direct-use",
          "label": "即时供能",
          "title": "光伏 → 充电站负荷",
          "rule": "在策略和设备允许时，光伏发电直接供给当前充电负载。",
          "activeFlows": [
            "pv-load"
          ]
        },
        {
          "id": "battery-shift",
          "label": "余电存储",
          "title": "光伏 → 储能系统",
          "rule": "当前充电需求用不完的光伏电量，可以先存入储能系统。",
          "activeFlows": [
            "pv-battery"
          ]
        },
        {
          "id": "delayed-use",
          "label": "延后供能",
          "title": "储能系统 → 充电站负荷",
          "rule": "储能系统可以在后续时段释放此前由光伏充入的电量，供给充电负载。",
          "activeFlows": [
            "battery-load"
          ]
        }
      ]
    },
    "boundary": {
      "coreTitle": "本地消纳边界",
      "coreCopy": "自发自用关注光伏电能是否在场站本地被消纳，可以通过储能平移使用时间；不承诺固定优先级、消纳比例或充电完成时间。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "充电站需量控制",
          "description": "需量控制看并网点功率峰值；自发自用看光伏电能是否在本地被充电负载消纳。"
        },
        {
          "term": "功率分配",
          "description": "功率分配是安排电能去向的过程，自发自用是其中围绕光伏本地消纳的运行目标。"
        },
        {
          "term": "电网充电后放电",
          "description": "电池电量来自电网时，后续放电不属于光伏自发自用链路。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "看懂光伏电能是直接供给充电负载，还是先存入储能后再使用。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注光伏、储能、充电负载和并网点之间的能量边界。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分光伏本地消纳、需量控制和其他功率策略，不把它们都概括成省电。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "光伏系统",
        "icon": "home",
        "href": "/terms/solar-storage-charging/pv-system/"
      },
      {
        "name": "储能系统",
        "icon": "battery",
        "href": "/terms/solar-storage-charging/energy-storage-system/"
      },
      {
        "name": "充电站需量控制",
        "icon": "gauge",
        "href": "/terms/solar-storage-charging/charging-station-demand-control/"
      },
      {
        "name": "功率分配",
        "icon": "gauge",
        "href": "/terms/solar-storage-charging/power-allocation/"
      }
    ],
    "sources": [
      {
        "label": "IEA PVPS",
        "title": "Review and Analysis of PV Self-Consumption Policies",
        "href": "https://iea-pvps.org/wp-content/uploads/2020/01/IEA-PVPS_-_Self-Consumption_Policies_-_2016_-_2.pdf"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "光储充一体化"
}
```

<a id="term-hybrid-inverter"></a>
## 混合光储逆变器 · 户用储能

```json
{
  "id": "term-hybrid-inverter",
  "sourceFile": "src/content/terms/hybrid-inverter.md",
  "sitePath": "/terms/hybrid-inverter/",
  "reviewRecord": {
    "termId": "term-hybrid-inverter",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "页面视觉、章节结构与拓扑交互已确认。",
      "概念定义、通俗解释、关键边界、角色视角和参考来源沿用当前正式页已确认内容。"
    ]
  },
  "content": {
    "id": "term-hybrid-inverter",
    "contentVersion": 1,
    "name": "混合光储逆变器",
    "english": "Hybrid Inverter",
    "termType": "device",
    "category": "户用储能",
    "summary": "理解混合光储逆变器在户用储能系统中的位置、作用与边界。",
    "definition": "同时具备光伏侧功率转换与电池双向功率转换能力，并连接光伏、电池、家庭负载和电网的设备。",
    "explanation": {
      "title": "通俗解释",
      "copy": "可同时把它理解成家庭储能系统中的“变电枢纽”：它转换光伏电能，配合电池充放电，并连接家庭负载和电网。"
    },
    "boundary": {
      "coreTitle": "核心边界",
      "coreCopy": "混合光储逆变器属于功率转换与系统连接设备，不等同于电池、BMS 或完整的能源管理系统。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "光伏逆变器",
          "description": "主要承担光伏侧功率转换；混合光储逆变器还具备与电池进行双向功率转换的能力。"
        },
        {
          "term": "储能逆变器",
          "description": "重点连接电池与交流侧；混合光储逆变器还可同时接入光伏侧。"
        },
        {
          "term": "PCS／储能变流器",
          "description": "PCS 描述电池直流电与交流电之间的双向变流功能，户用混合光储逆变器通常已经集成这项功能。"
        },
        {
          "term": "BMS／电池管理系统",
          "description": "负责电池监测、状态估算与保护，不承担主动功率转换。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "看懂电从哪里来、流向哪里，以及设备是否正常运行。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "确认设备连接关系、功率转换方向与系统协同边界。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "准确表达设备状态、功率方向和关联对象，避免概念混淆。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "电池系统",
        "icon": "battery"
      },
      {
        "name": "BMS／电池管理系统",
        "icon": "chip"
      },
      {
        "name": "SOC／电池荷电状态",
        "icon": "gauge",
        "href": "/terms/soc/"
      },
      {
        "name": "PCS／储能变流器",
        "icon": "chip",
        "href": "/terms/pcs/"
      }
    ],
    "sources": [
      {
        "title": "NREL technical report",
        "href": "https://www.nrel.gov/docs/fy17osti/67463.pdf"
      },
      {
        "label": "研究报告",
        "title": "Energy Storage Management Systems",
        "href": "https://www.sandia.gov/app/uploads/sites/163/2023/01/ESHB2020_Ch15_ESMS_Nguyen.pdf"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "户用储能"
}
```

<a id="term-pcs"></a>
## PCS／储能变流器 · 户用储能

```json
{
  "id": "term-pcs",
  "sourceFile": "src/content/terms/pcs.md",
  "sitePath": "/terms/pcs/",
  "reviewRecord": {
    "termId": "term-pcs",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "PCS 的双向变流功能与混合光储逆变器的集成关系已完成审阅确认。",
      "页面不表达具体厂商参数或工程接线结论。"
    ]
  },
  "content": {
    "id": "term-pcs",
    "contentVersion": 1,
    "name": "PCS／储能变流器",
    "english": "Power Conversion System",
    "termType": "device",
    "category": "户用储能",
    "summary": "理解 PCS 如何完成电池直流电与家庭或电网交流电之间的双向转换。",
    "definition": "PCS（储能变流器）负责电池直流电与家庭或电网交流电之间的双向转换；在户用储能中通常作为混合光储逆变器中的储能变流功能。",
    "explanation": {
      "title": "通俗解释",
      "copy": "PCS 就是一台双向“变电转换器”：专门负责电池直流电和家里／电网交流电之间互相转换，是储能充电、放电的动力执行部件。很多户用系统把这项功能集成在混合光储逆变器里。"
    },
    "boundary": {
      "coreTitle": "功能边界",
      "coreCopy": "PCS 描述储能变流功能，不代表家里一定要额外安装一台独立设备；户用混合光储逆变器通常已经包含这项功能。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "混合光储逆变器",
          "description": "混合光储逆变器还负责光伏侧转换和系统连接，通常集成电池双向转换功能。"
        },
        {
          "term": "电池系统",
          "description": "电池负责储存和释放电能，PCS 负责把直流电和交流电互相转换。"
        },
        {
          "term": "EMS／能量管理系统",
          "description": "EMS 根据供需和策略安排运行，PCS 按允许条件执行电能转换。"
        },
        {
          "term": "BMS／电池管理系统",
          "description": "BMS 提供电池状态和充放电允许条件，不承担主动功率转换。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "看懂电池如何通过转换为家庭负载供电，以及充电和放电的方向。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注交流侧、直流侧和电池允许条件之间的转换边界。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "清楚区分 PCS 这一变流功能与是否存在独立设备。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "混合光储逆变器",
        "icon": "battery",
        "href": "/terms/hybrid-inverter/"
      },
      {
        "name": "电池系统",
        "icon": "battery",
        "href": "/terms/battery-system/"
      },
      {
        "name": "EMS／能量管理系统",
        "icon": "chip",
        "href": "/terms/ems/"
      },
      {
        "name": "BMS／电池管理系统",
        "icon": "chip",
        "href": "/terms/bms/"
      }
    ],
    "sources": [
      {
        "label": "技术报告",
        "title": "Energy Storage Systems Integration",
        "href": "https://www.nrel.gov/docs/fy17osti/67463.pdf"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "户用储能"
}
```

<a id="term-self-consumption-ratio"></a>
## 自发自用率 · 户用储能

```json
{
  "id": "term-self-consumption-ratio",
  "sourceFile": "src/content/terms/self-consumption-ratio.md",
  "sitePath": "/terms/self-consumption-ratio/",
  "reviewRecord": {
    "termId": "term-self-consumption-ratio",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "采用用户侧消纳光伏电量除以光伏发电量的通用公式。",
      "页面不写入区域政策结论，统计周期、计量点和来源追踪保留为边界说明。",
      "公式语义、页面文案、关键边界和 IEA PVPS 参考来源已完成确认。"
    ]
  },
  "content": {
    "id": "term-self-consumption-ratio",
    "contentVersion": 1,
    "name": "自发自用率",
    "english": "Self-consumption Ratio (SCR)",
    "termType": "metric",
    "category": "户用储能",
    "summary": "理解统计周期内光伏发电量有多少在用户侧被消纳。",
    "definition": "自发自用率是统计周期内用户侧消纳的光伏电量占光伏发电量的比例。",
    "explanation": {
      "title": "通俗解释",
      "copy": "可以把自发自用率理解成光伏发电被用户侧留下并使用的“占比”：它回答的是发出来的光伏电量中，有多少在用户侧被消纳。"
    },
    "metricContent": {
      "formula": "自发自用率 = 用户侧消纳的光伏电量 ÷ 光伏发电量 × 100%"
    },
    "boundary": {
      "coreTitle": "统计边界",
      "coreCopy": "自发自用率只描述统计周期内光伏电量的用户侧消纳比例；统计周期、计量点和光伏电量来源追踪需要按具体系统口径确认。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "自给率／自足率",
          "description": "自发自用率以光伏发电量为分母；自给率或自足率通常关注负载用电中由本地光伏及储能满足的比例，问题方向不同。"
        },
        {
          "term": "统计周期",
          "description": "日、月、年等周期不同，发电量与用户侧消纳量的汇总结果也会不同。"
        },
        {
          "term": "计量点与来源追踪",
          "description": "需要明确光伏发电量、即时自用量和光伏充电后放电量的计量位置与来源追踪方式。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "用一个比例看懂光伏发电有多少最终在用户侧被使用，而不是只看瞬时功率。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "确认统计周期、计量点和电池充电来源，保证分子与分母处于同一口径。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "明确展示指标的统计范围，并把自发自用率和自给率等相近指标分开命名。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "自发自用",
        "icon": "home",
        "href": "/terms/self-consumption/"
      },
      {
        "name": "电池系统",
        "icon": "battery",
        "href": "/terms/battery-system/"
      },
      {
        "name": "SOC／电池荷电状态",
        "icon": "gauge",
        "href": "/terms/soc/"
      },
      {
        "name": "混合光储逆变器",
        "icon": "battery",
        "href": "/terms/hybrid-inverter/"
      }
    ],
    "sources": [
      {
        "label": "IEA PVPS",
        "title": "Review and Analysis of PV Self-Consumption Policies",
        "href": "https://iea-pvps.org/wp-content/uploads/2020/01/IEA-PVPS_-_Self-Consumption_Policies_-_2016_-_2.pdf"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "户用储能"
}
```

<a id="term-islanded-operation"></a>
## 孤岛运行 · 户用储能

```json
{
  "id": "term-islanded-operation",
  "sourceFile": "src/content/terms/islanded-operation.md",
  "sitePath": "/terms/islanded-operation/",
  "reviewRecord": {
    "termId": "term-islanded-operation",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "英文正式名采用 Islanded Operation，Island Mode 作为搜索别名。",
      "并网、隔离、孤岛运行和备电策略的边界，以及 DOE 参考来源已完成确认。"
    ]
  },
  "content": {
    "id": "term-islanded-operation",
    "contentVersion": 1,
    "name": "孤岛运行",
    "english": "Islanded Operation",
    "aliases": [
      "Island Mode"
    ],
    "termType": "state",
    "category": "户用储能",
    "summary": "理解电网断开后光伏、储能和负载如何在本地运行。",
    "definition": "电网断开后，光伏、储能和负载在本地独立供电的状态。",
    "definitionNote": "Island Mode 是常见的英文表达。",
    "explanation": {
      "title": "通俗解释",
      "copy": "孤岛运行可以理解为“家里暂时自己供电”：系统与公共电网断开，由本地可用的光伏、储能和其他电源继续给负载供电。"
    },
    "boundary": {
      "coreTitle": "状态边界",
      "coreCopy": "孤岛运行是电网断开后的运行状态，不是一种电量预留策略；系统必须先与公共电网隔离，才能向本地负载独立供电。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "备电模式",
          "description": "决定平时保留多少电、优先供哪些负载；孤岛运行描述断网后的实际状态。"
        },
        {
          "term": "并网运行",
          "description": "系统与公共电网保持连接时的运行状态。"
        },
        {
          "term": "混合光储逆变器",
          "description": "是否能进入和维持孤岛运行，取决于逆变器功率、隔离能力和系统配置。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解停电后系统为什么要与电网断开，以及哪些负载还能继续供电。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注隔离、并网恢复、负载范围和光伏储能的可用状态。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分运行状态、备电策略和设备能力，不把孤岛运行写成电量预留。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "备电模式",
        "icon": "home",
        "href": "/terms/backup-mode/"
      },
      {
        "name": "混合光储逆变器",
        "icon": "battery",
        "href": "/terms/hybrid-inverter/"
      },
      {
        "name": "电池系统",
        "icon": "battery",
        "href": "/terms/battery-system/"
      },
      {
        "name": "EMS／能量管理系统",
        "icon": "chip",
        "href": "/terms/ems/"
      }
    ],
    "sources": [
      {
        "label": "U.S. Department of Energy",
        "title": "Microgrid Systems",
        "href": "https://www.energy.gov/oe/microgrid-systems"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "户用储能"
}
```

<a id="term-soc"></a>
## SOC／电池荷电状态 · 户用储能

```json
{
  "id": "term-soc",
  "sourceFile": "src/content/terms/soc.md",
  "sitePath": "/terms/soc/",
  "reviewRecord": {
    "termId": "term-soc",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "采用连续 0%～100% 示意刻度，不定义低、中、高阈值。",
      "SOC 通用定义、页面文案、关键边界和 DOE/EPRI 参考来源已完成确认。"
    ]
  },
  "content": {
    "id": "term-soc",
    "contentVersion": 1,
    "name": "SOC／电池荷电状态",
    "english": "State of Charge",
    "termType": "state",
    "category": "户用储能",
    "summary": "理解 SOC 如何表示电池当前相对于参考满电容量的荷电程度。",
    "definition": "SOC（State of Charge，电池荷电状态）表示电池当前相对于参考满电容量的荷电程度，通常以百分比表示；它是基于测量和估算得到的状态量，不等同于 SOH、可用容量或允许功率。",
    "explanation": {
      "title": "通俗解释",
      "copy": "可以把 SOC 理解成电池系统的“剩余电量指示器”：它用百分比表达当前相对于参考满电状态的位置，充电时通常上升，放电时通常下降。"
    },
    "stateContent": {
      "defaultValue": 50,
      "chargeCopy": "充电时，SOC 通常向满电参考状态移动。",
      "dischargeCopy": "放电时，SOC 通常向低荷电参考状态移动。"
    },
    "boundary": {
      "coreTitle": "状态边界",
      "coreCopy": "SOC 是描述当前荷电程度的状态量，不直接等同于电池健康程度、可用电量或当前允许的充放电功率。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "SOH／电池健康度",
          "description": "SOH 描述相对于参考状态的健康程度，SOC 描述当前荷电位置。"
        },
        {
          "term": "剩余电量／可用容量",
          "description": "SOC 是相对比例；剩余电量或可用容量还取决于参考容量、当前条件和系统口径。"
        },
        {
          "term": "允许功率",
          "description": "允许功率表示当前可以充放电的功率范围，可能受 SOC、温度、健康状态和保护条件共同影响。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "看懂电池当前大致处于什么荷电位置，以及充放电后状态如何变化。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注 SOC 的估算口径、参考容量和系统保护条件，不把示意值当作统一阈值。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "将 SOC 表达为状态信息，和 SOH、可用容量、允许功率等字段明确区分。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "BMS／电池管理系统",
        "icon": "chip",
        "href": "/terms/bms/"
      },
      {
        "name": "电池系统",
        "icon": "battery",
        "href": "/terms/battery-system/"
      },
      {
        "name": "混合光储逆变器",
        "icon": "battery",
        "href": "/terms/hybrid-inverter/"
      },
      {
        "name": "自发自用",
        "icon": "home",
        "href": "/terms/self-consumption/"
      }
    ],
    "sources": [
      {
        "label": "储能术语表",
        "title": "Electricity Storage Handbook 2013",
        "href": "https://www.energy.gov/sites/default/files/2013/08/f2/ElecStorageHndbk2013.pdf"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "户用储能"
}
```

<a id="term-soh"></a>
## SOH／电池健康度 · 户用储能

```json
{
  "id": "term-soh",
  "sourceFile": "src/content/terms/soh.md",
  "sitePath": "/terms/soh/",
  "reviewRecord": {
    "termId": "term-soh",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "SOH 与 SOC、容量和剩余寿命的边界已完成审阅确认。",
      "容量示意只用于说明“充满不等于容量相同”，不代表具体 SOH 数值。"
    ]
  },
  "content": {
    "id": "term-soh",
    "contentVersion": 1,
    "name": "SOH／电池健康度",
    "english": "State of Health",
    "termType": "state",
    "category": "户用储能",
    "summary": "理解 SOH 如何描述电池相对于参考状态的健康程度。",
    "definition": "SOH（State of Health，电池健康度）反映电池相对于参考状态的健康程度，具体含义取决于评价口径。",
    "explanation": {
      "title": "通俗解释",
      "copy": "SOH 像电池的“健康评分”。SOC 看“现在充得多满”，SOH 看“性能保持得怎样”。充满电，不代表恢复了健康度。"
    },
    "boundary": {
      "coreTitle": "状态边界",
      "coreCopy": "SOH 描述电池相对于参考状态的健康程度，不等同于当前荷电程度、剩余寿命或单独的安全结论。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "SOC／电池荷电状态",
          "description": "SOC 看当前电池充得多满，SOH 看电池性能相对参考状态保持得怎样。"
        },
        {
          "term": "剩余寿命",
          "description": "SOH 是一种健康度指标，不直接给出还能使用多久。"
        },
        {
          "term": "电池容量",
          "description": "SOH 的具体口径可能参考容量、功率或其他评价指标，需要结合评价条件理解。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解即使当前显示充满，电池可用容量也可能已与参考状态不同。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注评价指标、参考条件和估算口径，不把示意图当作统一数值标准。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分健康度、荷电状态和容量；未知值不应被显示为零。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "SOC／电池荷电状态",
        "icon": "gauge",
        "href": "/terms/soc/"
      },
      {
        "name": "BMS／电池管理系统",
        "icon": "chip",
        "href": "/terms/bms/"
      },
      {
        "name": "电池系统",
        "icon": "battery",
        "href": "/terms/battery-system/"
      },
      {
        "name": "EMS／能量管理系统",
        "icon": "chip",
        "href": "/terms/ems/"
      }
    ],
    "sources": [
      {
        "title": "SOH 评价口径研究",
        "href": "https://arxiv.org/abs/2508.15517"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "户用储能"
}
```

<a id="term-backup-mode"></a>
## 备电模式 · 户用储能

```json
{
  "id": "term-backup-mode",
  "sourceFile": "src/content/terms/backup-mode.md",
  "sitePath": "/terms/backup-mode/",
  "reviewRecord": {
    "termId": "term-backup-mode",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "备电模式定位为策略，重点说明电量预留和重要负载优先级。",
      "与孤岛运行的策略／状态边界、SOC 关系和 SMA 参考来源已完成确认。"
    ]
  },
  "content": {
    "id": "term-backup-mode",
    "contentVersion": 1,
    "name": "备电模式",
    "english": "Backup Mode",
    "termType": "strategy",
    "category": "户用储能",
    "summary": "理解备电预留如何在停电时优先保障重要负载。",
    "definition": "提前留出一部分电量，停电时优先保障重要负载。",
    "explanation": {
      "title": "通俗解释",
      "copy": "备电模式像给停电留一份“备用电”。它决定平时要保留多少电，以及停电后优先供哪些负载。"
    },
    "boundary": {
      "coreTitle": "策略边界",
      "coreCopy": "备电模式是预先设定的策略，用来安排电量预留和供电优先级，不代表当前已经停电。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "孤岛运行",
          "description": "描述电网断开后的本地供电状态，不是电量预留策略。"
        },
        {
          "term": "自发自用",
          "description": "优先消纳光伏电量，但要遵守备电模式设定的 SOC 预留。"
        },
        {
          "term": "SOC／电池荷电状态",
          "description": "SOC 反映当前荷电程度，备电模式决定需要保留到什么范围。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解为什么电池不会一直放到最低，以及停电时哪些负载优先供电。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注备电预留、重要负载、逆变器功率和电池状态之间的约束。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "清楚区分备电策略与停电后的实际运行状态，不把预留电量写成当前供电结果。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "孤岛运行",
        "icon": "home",
        "href": "/terms/islanded-operation/"
      },
      {
        "name": "SOC／电池荷电状态",
        "icon": "gauge",
        "href": "/terms/soc/"
      },
      {
        "name": "混合光储逆变器",
        "icon": "battery",
        "href": "/terms/hybrid-inverter/"
      },
      {
        "name": "EMS／能量管理系统",
        "icon": "chip",
        "href": "/terms/ems/"
      }
    ],
    "sources": [
      {
        "label": "SMA",
        "title": "Backup Planning Guide",
        "href": "https://files.sma.de/downloads/SI-SBS-STPSE-Backup-PL-en-30.pdf"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "户用储能"
}
```

<a id="term-peak-shaving"></a>
## 负载削峰 · 户用储能

```json
{
  "id": "term-peak-shaving",
  "sourceFile": "src/content/terms/peak-shaving.md",
  "sitePath": "/terms/peak-shaving/",
  "reviewRecord": {
    "termId": "term-peak-shaving",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "负载削峰定位为功率目标，明确与峰谷套利和自发自用的关系。",
      "功率上限、SOC 约束和 SMA 参考来源已完成确认。"
    ]
  },
  "content": {
    "id": "term-peak-shaving",
    "contentVersion": 1,
    "name": "负载削峰",
    "english": "Peak Shaving",
    "termType": "strategy",
    "category": "户用储能",
    "summary": "理解如何用电池压低电网侧瞬时功率峰值。",
    "definition": "压低家里某一时刻从电网取电的最大功率。",
    "explanation": {
      "title": "通俗解释",
      "copy": "当多个大功率设备同时运行时，电池补一部分电，让电网侧功率尽量不超过设定上限。"
    },
    "boundary": {
      "coreTitle": "功率目标",
      "coreCopy": "负载削峰关注功率峰值，重点是压低电网侧瞬时功率，不等于减少家庭总用电量。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "峰谷套利",
          "description": "看电价时段安排充放电，重点是电价目标，不是瞬时功率上限。"
        },
        {
          "term": "自发自用",
          "description": "优先消纳光伏电量；削峰的触发依据是电网侧功率上限。"
        },
        {
          "term": "SOC／电池荷电状态",
          "description": "电池要有足够的 SOC 和放电功率，才能补上瞬时负载。"
        },
        {
          "term": "策略关系",
          "description": "负载削峰看功率峰值，峰谷套利看电价时段；自发自用优先消纳光伏电量，能否叠加及优先级以系统设定为准。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解为什么大功率设备同时运行时电池会放电，以及电网侧峰值如何降低。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注电网侧功率上限、电池可用功率和设备响应条件。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分功率目标、电价目标和自发自用目标，不把削峰写成减少总用电量。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "峰谷套利",
        "icon": "gauge",
        "href": "/terms/peak-valley-arbitrage/"
      },
      {
        "name": "自发自用",
        "icon": "home",
        "href": "/terms/self-consumption/"
      },
      {
        "name": "SOC／电池荷电状态",
        "icon": "gauge",
        "href": "/terms/soc/"
      },
      {
        "name": "EMS／能量管理系统",
        "icon": "chip",
        "href": "/terms/ems/"
      }
    ],
    "sources": [
      {
        "label": "SMA",
        "title": "Peak Load Shaving Function",
        "href": "https://manuals.sma.de/SBSxx-US-10/en-US/391139595.html"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "户用储能"
}
```

<a id="term-peak-valley-arbitrage"></a>
## 峰谷套利 · 户用储能

```json
{
  "id": "term-peak-valley-arbitrage",
  "sourceFile": "src/content/terms/peak-valley-arbitrage.md",
  "sitePath": "/terms/peak-valley-arbitrage/",
  "reviewRecord": {
    "termId": "term-peak-valley-arbitrage",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "峰谷套利定位为电价目标，明确与负载削峰和自发自用的关系。",
      "电价差、损耗、可用电量边界和 DOE 参考来源已完成确认。"
    ]
  },
  "content": {
    "id": "term-peak-valley-arbitrage",
    "contentVersion": 1,
    "name": "峰谷套利",
    "english": "Peak-valley Arbitrage",
    "termType": "strategy",
    "category": "户用储能",
    "summary": "理解如何按峰谷电价安排储能充放电。",
    "definition": "低电价时充电，高电价时放电，利用时段价差减少购电成本。",
    "explanation": {
      "title": "通俗解释",
      "copy": "峰谷套利看的是电价时段：低价时先存电，高价时再用电；是否能产生实际节省，还要看电价差、损耗和系统设置。"
    },
    "boundary": {
      "coreTitle": "电价目标",
      "coreCopy": "峰谷套利关注电价和时间，需要适用的峰谷电价与允许的充放电策略，不承诺固定收益。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "负载削峰",
          "description": "看电网侧功率峰值；峰谷套利看电价时段。"
        },
        {
          "term": "自发自用",
          "description": "优先消纳光伏电量；峰谷套利主要利用低价与高价时段的差异。"
        },
        {
          "term": "SOC／电池荷电状态",
          "description": "可用电量和 SOC 会限制低价充电、高价放电的实际执行范围。"
        },
        {
          "term": "策略关系",
          "description": "峰谷套利看电价时段，负载削峰看功率峰值；自发自用优先消纳光伏电量，能否叠加及优先级以系统设定为准。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解为什么系统会在低价时段充电、高价时段放电，以及节省会受哪些条件影响。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注峰谷时段、电价差、充放电损耗和电池可用电量。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分电价策略、功率策略和自发自用策略，不绑定具体地区电价或收益承诺。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "负载削峰",
        "icon": "gauge",
        "href": "/terms/peak-shaving/"
      },
      {
        "name": "自发自用",
        "icon": "home",
        "href": "/terms/self-consumption/"
      },
      {
        "name": "SOC／电池荷电状态",
        "icon": "gauge",
        "href": "/terms/soc/"
      },
      {
        "name": "EMS／能量管理系统",
        "icon": "chip",
        "href": "/terms/ems/"
      }
    ],
    "sources": [
      {
        "label": "U.S. Department of Energy",
        "title": "Energy Storage Valuation",
        "href": "https://www.energy.gov/sites/default/files/2022-06/MSP_Report_2022June_Final_508_v3.pdf"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "户用储能"
}
```

<a id="term-self-consumption"></a>
## 自发自用 · 户用储能

```json
{
  "id": "term-self-consumption",
  "sourceFile": "src/content/terms/self-consumption.md",
  "sitePath": "/terms/self-consumption/",
  "reviewRecord": {
    "termId": "term-self-consumption",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "采用光伏用户侧闭环消纳并允许电池时间平移的广义口径。",
      "电网充电后放电明确排除出光伏自发自用链路，情境文案与参考来源已完成确认。"
    ]
  },
  "content": {
    "id": "term-self-consumption",
    "contentVersion": 1,
    "name": "自发自用",
    "english": "Self-consumption",
    "termType": "strategy",
    "category": "户用储能",
    "summary": "理解光伏电能如何在用户侧优先消纳，并通过电池实现时间平移。",
    "definition": "自发自用是指光伏电能在用户侧被本地负载消纳，既可以在发电时直接使用，也可以先由光伏充入电池、在后续时段再放电供给本地负载。",
    "explanation": {
      "title": "通俗解释",
      "copy": "可以把自发自用理解成光伏电能的“就地消纳”：光伏电能先服务家庭负载，暂时用不完的部分存入电池，之后再供给家庭负载。"
    },
    "strategyContent": {
      "scenarios": [
        {
          "id": "direct-use",
          "label": "即时自用",
          "title": "光伏 → 家庭负载",
          "rule": "光伏发电优先在当前时段供给家庭负载。",
          "activeFlows": [
            "pv-load"
          ]
        },
        {
          "id": "battery-shift",
          "label": "余电存储",
          "title": "光伏 → 电池系统",
          "rule": "当前负载用不完的光伏电能可以先存入电池，为后续使用做准备。",
          "activeFlows": [
            "pv-battery"
          ]
        },
        {
          "id": "delayed-use",
          "label": "延后自用",
          "title": "电池系统 → 家庭负载",
          "rule": "电池将此前由光伏充入的电能在后续时段供给家庭负载。",
          "activeFlows": [
            "battery-load"
          ]
        }
      ]
    },
    "boundary": {
      "coreTitle": "闭环边界",
      "coreCopy": "自发自用关注光伏电能是否在用户侧被消纳，允许通过电池把使用时间向后平移；电网充电后再放电不属于光伏自发自用链路。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "即时自用",
          "description": "光伏发电时直接供给家庭负载，是自发自用的实时消纳方式。"
        },
        {
          "term": "光伏余电充电",
          "description": "当前用不完的光伏电能进入电池，之后再供给家庭负载，仍属于用户侧闭环消纳。"
        },
        {
          "term": "电网充电后放电",
          "description": "电池电能来自电网时，后续放电属于其他运行策略，不计入光伏自发自用链路。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "看懂光伏电能是直接供家里使用，还是先存入电池再延后使用。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注光伏、电池和家庭负载的能量方向，以及电池充电来源是否可追踪。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "清楚区分光伏闭环消纳和电网套利等其他策略，避免只用“省电”概括不同机制。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "混合光储逆变器",
        "icon": "battery",
        "href": "/terms/hybrid-inverter/"
      },
      {
        "name": "电池系统",
        "icon": "battery",
        "href": "/terms/battery-system/"
      },
      {
        "name": "SOC／电池荷电状态",
        "icon": "gauge",
        "href": "/terms/soc/"
      },
      {
        "name": "自发自用率",
        "icon": "gauge",
        "href": "/terms/self-consumption-ratio/"
      }
    ],
    "sources": [
      {
        "label": "IEA PVPS",
        "title": "Review and Analysis of PV Self-Consumption Policies",
        "href": "https://iea-pvps.org/wp-content/uploads/2020/01/IEA-PVPS_-_Self-Consumption_Policies_-_2016_-_2.pdf"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "户用储能"
}
```

<a id="term-battery-system"></a>
## 电池系统 · 户用储能

```json
{
  "id": "term-battery-system",
  "sourceFile": "src/content/terms/battery-system.md",
  "sitePath": "/terms/battery-system/",
  "reviewRecord": {
    "termId": "term-battery-system",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "电池系统定义采用电芯、模组或电池包、BMS、电气保护和必要热管理部件组成的行业通用表述。",
      "产品边界差异通过定义旁注说明，不以待确认文案常驻展示。",
      "系统关系、核心职责节点交互、数据维度、场景说明和角色视角已接入系统类共享模板。",
      "参考来源使用一条代表性官方标准详情链接，公开页面默认展示一条来源。"
    ]
  },
  "content": {
    "id": "term-battery-system",
    "contentVersion": 1,
    "name": "电池系统",
    "english": "Battery System",
    "termType": "system",
    "category": "户用储能",
    "summary": "电池系统是由电芯、模组或电池包、BMS、电气保护和必要的热管理部件组成的储能主体，负责以直流电形式存储和释放能量，并向上层控制系统提供可用功率、容量和安全边界。",
    "definition": "电池系统是由电芯、模组或电池包、BMS、电气保护和必要的热管理部件组成的储能主体，负责以直流电形式存储和释放能量，并向上层控制系统提供可用功率、容量和安全边界。",
    "definitionNote": "不同产品的电池系统边界可能对应电池包、电池簇或电池柜等层级，具体以产品技术文件中的结构定义为准。",
    "explanation": {
      "title": "通俗解释",
      "copy": "可以把电池系统理解成储能设备里的“储钱罐加安全管家”：电芯和电池包负责存电，BMS、保护和热管理负责判断什么时候能安全充放电。PCS、逆变器和 EMS 是外部协作设备，不属于电池系统本体。"
    },
    "systemContent": {
      "responsibilities": [
        "存储和释放电能，并提供可用容量与充放电功率边界。",
        "由 BMS 采集电压、温度和电流，估算 SOC、SOH 等状态。",
        "在过压、欠压、过温、过流或绝缘异常时限制或停止充放电。",
        "向逆变器、PCS、EMS 或运维平台提供状态、告警和允许功率。"
      ],
      "dataDimensions": [
        {
          "name": "额定容量与可用容量",
          "description": "描述电池系统的标称储能能力和当前允许使用的容量范围。"
        },
        {
          "name": "SOC",
          "description": "表示当前剩余电量状态，依赖 BMS 的估算口径。"
        },
        {
          "name": "SOH",
          "description": "表示相对于参考状态的健康程度，通常随老化缓慢变化。"
        },
        {
          "name": "充放电功率边界",
          "description": "表示当前允许的最大充电和放电功率，受 SOC、温度、健康状态和保护状态影响。"
        },
        {
          "name": "电压、电流与温度",
          "description": "用于监测运行状态、计算功率并判断安全边界。"
        },
        {
          "name": "保护与告警状态",
          "description": "表示过压、欠压、过流、过温、绝缘或通信等异常状态。"
        }
      ],
      "scenarios": [
        {
          "name": "户用储能",
          "description": "连接混合光储逆变器，为家庭提供储能与备电。"
        },
        {
          "name": "工商业储能",
          "description": "通过 PCS 接入园区交流侧，按 EMS 目标充放电。"
        },
        {
          "name": "大型储能",
          "description": "由多个电池簇或电池舱组成，与 PCS、EMS 共同构成储能电站。"
        }
      ],
      "topologyBindings": [
        {
          "sceneId": "scene-residential-storage",
          "topologyId": "hybrid-storage",
          "isPrimary": true,
          "verificationStatus": "unverified",
          "evidenceRefs": []
        },
        {
          "sceneId": "scene-residential-storage",
          "topologyId": "ac-coupled-storage",
          "isPrimary": false,
          "verificationStatus": "unverified",
          "evidenceRefs": []
        },
        {
          "sceneId": "scene-commercial-storage",
          "topologyId": "commercial-ac-storage",
          "isPrimary": true,
          "verificationStatus": "unverified",
          "evidenceRefs": []
        },
        {
          "sceneId": "scene-large-scale-storage",
          "topologyId": "grid-scale-storage",
          "isPrimary": true,
          "verificationStatus": "unverified",
          "evidenceRefs": []
        }
      ]
    },
    "boundary": {
      "coreTitle": "系统边界",
      "coreCopy": "电池系统边界包括电芯或电池包、BMS、内部电气连接、保护器件以及产品范围内的热管理部件。PCS 或混合光储逆变器负责功率变换，EMS 负责站点或系统级策略，二者不属于电池系统本体。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "单个电芯",
          "description": "电池系统不是单个电芯，而是由电芯、模组或电池包及管理、保护部件共同构成的储能主体。"
        },
        {
          "term": "PCS／逆变器",
          "description": "PCS 或混合光储逆变器负责功率变换，不属于电池系统本体。"
        },
        {
          "term": "EMS",
          "description": "EMS 负责站点或系统级策略，不属于电池系统本体。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "判断电池系统当前是否可用、是否允许充放电，以及异常是否需要处理。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "确认电池系统与 BMS、逆变器和 EMS 的连接关系及安全边界。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分电池系统、BMS、功率转换和策略管理的职责，避免把状态、告警和允许功率混为一谈。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "BMS／电池管理系统",
        "icon": "chip"
      },
      {
        "name": "SOC／电池荷电状态",
        "icon": "gauge",
        "href": "/terms/soc/"
      },
      {
        "name": "SOH／电池健康度",
        "icon": "gauge",
        "href": "/terms/soh/"
      },
      {
        "name": "混合光储逆变器",
        "icon": "battery",
        "href": "/terms/hybrid-inverter/"
      }
    ],
    "sources": [
      {
        "title": "DL/T 5903-2025《户用电化学储能系统设计规范》",
        "href": "https://std.samr.gov.cn/hb/search/stdHBDetailed?id=461E291C92D3AB7EE06397BE0A0A7DFF"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "户用储能"
}
```

<a id="term-bms"></a>
## BMS／电池管理系统 · 户用储能

```json
{
  "id": "term-bms",
  "sourceFile": "src/content/terms/bms.md",
  "sitePath": "/terms/bms/",
  "reviewRecord": {
    "termId": "term-bms",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "BMS 内容、边界、拓扑关系和 GB/T 34131-2023 来源已完成审阅确认。",
      "系统关系图按信息、保护和控制关系建模，不展示能源流。",
      "相关术语限制为 4 个，不展示 SOE；正式页默认展示一条来源。"
    ]
  },
  "content": {
    "id": "term-bms",
    "contentVersion": 1,
    "name": "BMS／电池管理系统",
    "english": "Battery Management System",
    "termType": "system",
    "category": "户用储能",
    "summary": "理解 BMS 如何监测、估算、保护并管理电池系统的运行状态。",
    "definition": "BMS（电池管理系统）是对电池系统进行监测、状态估算、保护和通信管理的控制系统，负责根据电池状态判断充放电条件，并向上层设备提供状态、告警和允许功率。",
    "definitionNote": "不同产品的 BMS 功能可能由电池包级、簇级或多级控制器共同实现，具体边界以产品技术文件中的结构定义为准。",
    "explanation": {
      "title": "通俗解释",
      "copy": "可以把 BMS 理解成电池系统的“监测与安全管家”：它持续读取电压、电流和温度等信息，判断电池状态，在异常时限制或停止充放电，并把状态、告警和允许功率提供给上层设备。"
    },
    "systemContent": {
      "responsibilities": [
        "采集电芯、模组或电池包的电压、电流、温度等运行信息。",
        "估算 SOC、SOH 等电池状态，为充放电控制提供依据。",
        "根据保护条件限制或停止充放电，管理异常和告警状态。",
        "向逆变器、PCS、EMS 或运维平台提供状态、告警和允许功率。"
      ],
      "dataDimensions": [
        {
          "name": "电压、电流与温度",
          "description": "用于监测电池运行状态，并为功率计算和安全判断提供基础数据。"
        },
        {
          "name": "SOC",
          "description": "表示当前剩余电量状态，依赖 BMS 的估算口径。"
        },
        {
          "name": "SOH",
          "description": "表示相对于参考状态的健康程度，通常随电池老化缓慢变化。"
        },
        {
          "name": "保护与告警状态",
          "description": "表示过压、欠压、过流、过温、绝缘或通信等异常状态。"
        },
        {
          "name": "充放电允许与功率边界",
          "description": "表示当前是否允许充放电，以及受状态和保护条件约束的功率范围。"
        }
      ],
      "scenarios": [
        {
          "name": "户用储能",
          "description": "监测电池状态，协调充放电保护，并向混合光储逆变器提供允许状态。"
        },
        {
          "name": "工商业储能",
          "description": "管理电池簇状态与保护，通过 PCS 交换状态和允许功率。"
        },
        {
          "name": "大型储能",
          "description": "汇总电池簇或电池舱状态，向上层系统提供监测、告警与保护信息。"
        }
      ],
      "topologyBindings": [
        {
          "sceneId": "scene-residential-storage",
          "topologyId": "bms-system",
          "isPrimary": true,
          "verificationStatus": "verified",
          "evidenceRefs": []
        }
      ]
    },
    "boundary": {
      "coreTitle": "系统边界",
      "coreCopy": "BMS 是电池系统中的监测、估算、保护与通信管理子系统，不是储能电芯本体，也不负责把直流电转换为交流电或制定站点级运行策略。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "电池系统",
          "description": "电池系统是由储能部件及管理、保护等部件组成的整体；BMS 是其中负责监测、估算和保护的管理子系统。"
        },
        {
          "term": "电芯／模组",
          "description": "电芯和模组负责储存、释放电能；BMS 负责采集状态并执行管理与保护。"
        },
        {
          "term": "PCS／逆变器",
          "description": "PCS 或逆变器负责功率变换，BMS 提供电池状态和允许功率，不承担主动功率转换。"
        },
        {
          "term": "EMS",
          "description": "EMS 负责站点或系统级策略，BMS 负责电池侧状态、保护和充放电条件。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "看懂 SOC、SOH、告警和充放电允许状态，判断电池当前是否可用。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "确认采集、通信、保护器件和充放电联锁关系，关注异常条件下的安全边界。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分测量、估算、保护、告警和允许功率，避免把 BMS 表达成电池或逆变器功能。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "电池系统",
        "icon": "battery",
        "href": "/terms/battery-system/"
      },
      {
        "name": "SOC／电池荷电状态",
        "icon": "gauge",
        "href": "/terms/soc/"
      },
      {
        "name": "SOH／电池健康度",
        "icon": "gauge",
        "href": "/terms/soh/"
      },
      {
        "name": "混合光储逆变器",
        "icon": "battery",
        "href": "/terms/hybrid-inverter/"
      }
    ],
    "sources": [
      {
        "title": "GB/T 34131-2023《电力储能用电池管理系统》",
        "href": "https://std.samr.gov.cn/gb/search/gbDetailed?id=39999368335A6512E06397BE0A0A284B"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "户用储能"
}
```

<a id="term-ems"></a>
## EMS／能量管理系统 · 户用储能

```json
{
  "id": "term-ems",
  "sourceFile": "src/content/terms/ems.md",
  "sitePath": "/terms/ems/",
  "reviewRecord": {
    "termId": "term-ems",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "EMS 的信息输入、调度和设备协同关系已完成审阅确认。",
      "内容仅覆盖户用储能，不把功能关系表达为实际通信接线。"
    ]
  },
  "content": {
    "id": "term-ems",
    "contentVersion": 1,
    "name": "EMS／能量管理系统",
    "english": "Energy Management System",
    "termType": "system",
    "category": "户用储能",
    "summary": "理解 EMS 如何结合供需、设备状态和设定策略安排家庭储能运行。",
    "definition": "EMS（能量管理系统）根据能源供需、设备状态和设定策略，在设备允许条件下协调家庭储能系统运行。",
    "explanation": {
      "title": "通俗解释",
      "copy": "EMS 就是整套光伏储能家里的“智能管家＋调度大脑”：它盯着发电、用电和电池情况，自动安排什么时候充电、什么时候放电。"
    },
    "systemContent": {
      "responsibilities": [
        "EMS 接收信息并安排运行。",
        "混合光储逆变器执行电能转换，并反馈运行情况。",
        "BMS 为 EMS 和逆变器提供电池状态与充放电允许条件。"
      ],
      "dataDimensions": [
        {
          "name": "发电与用电信息",
          "description": "为运行安排提供当前的发电和用电情况。"
        },
        {
          "name": "电池状态与允许条件",
          "description": "反映 SOC、功率边界和保护条件，决定当前能否充放电。"
        },
        {
          "name": "设定策略",
          "description": "指定自发自用、备电等运行目标。"
        },
        {
          "name": "执行反馈",
          "description": "反馈设备是否按运行目标执行。"
        }
      ],
      "scenarios": [
        {
          "name": "自发自用",
          "description": "EMS 根据光伏、负载和电池状态安排优先消纳。"
        },
        {
          "name": "备电预留",
          "description": "EMS 在日常运行中遵守预留电量，保留停电时的可用电量。"
        }
      ],
      "topologyBindings": [
        {
          "sceneId": "home-energy-storage",
          "topologyId": "ems-relations",
          "isPrimary": true,
          "verificationStatus": "verified",
          "evidenceRefs": [
            "ems-home-storage"
          ]
        }
      ]
    },
    "boundary": {
      "coreTitle": "系统边界",
      "coreCopy": "EMS 负责结合信息和策略安排运行，实际执行仍受逆变器能力、电池状态和保护条件约束。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "BMS／电池管理系统",
          "description": "BMS 管理电池状态、保护和充放电允许条件；EMS 根据这些条件安排系统运行。"
        },
        {
          "term": "PCS／储能变流器",
          "description": "PCS 负责电池直流电和交流电之间的双向转换；EMS 负责运行安排。"
        },
        {
          "term": "混合光储逆变器",
          "description": "混合光储逆变器执行光伏和电池的功率转换，很多产品已集成 PCS 功能。"
        },
        {
          "term": "独立设备",
          "description": "EMS 不一定是单独一台设备，也不一定依赖 AI 或云端。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "看懂系统为什么在当前时刻充电、放电或保留电量。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注调度目标与设备能力、电池允许条件之间的配合。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分运行策略、调度目标和设备实际执行状态。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "BMS／电池管理系统",
        "icon": "chip",
        "href": "/terms/bms/"
      },
      {
        "name": "PCS／储能变流器",
        "icon": "chip",
        "href": "/terms/pcs/"
      },
      {
        "name": "混合光储逆变器",
        "icon": "battery",
        "href": "/terms/hybrid-inverter/"
      },
      {
        "name": "自发自用",
        "icon": "home",
        "href": "/terms/self-consumption/"
      }
    ],
    "sources": [
      {
        "title": "SMA 户用能源管理资料",
        "href": "https://www.sma.de/en/products/energy-management/sunny-home-manager"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "户用储能"
}
```

<a id="term-utility-capacity-lease"></a>
## 容量租赁 · 大型储能

```json
{
  "id": "term-utility-capacity-lease",
  "sourceFile": "src/content/terms/utility-capacity-lease.md",
  "sitePath": "/terms/utility-scale-storage/capacity-lease/",
  "reviewRecord": {
    "termId": "term-utility-capacity-lease",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "已确认容量租赁表达服务组织方式，不表达固定收益或合同结论。"
    ]
  },
  "content": {
    "id": "term-utility-capacity-lease",
    "contentVersion": 1,
    "scene": "utility-scale-storage",
    "name": "容量租赁",
    "english": "Capacity Leasing",
    "termType": "strategy",
    "category": "容量服务",
    "summary": "说明储能可用容量或服务能力如何被其他主体安排使用。",
    "definition": "容量租赁是围绕储能可用功率、电量或服务能力形成的组织与服务安排，具体的容量口径、调用方式和结算条件取决于合同与适用规则。",
    "explanation": {
      "title": "通俗解释",
      "copy": "容量租赁可以理解成“租用储能的可用能力”：租用方获得约定的功率或电量服务，储能电站仍按实际状态和规则执行。"
    },
    "boundary": {
      "coreTitle": "服务边界",
      "coreCopy": "容量租赁讲的是容量和服务如何组织，不代表固定收益、固定调用次数或统一的合同模板。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "独立储能",
          "description": "独立储能描述项目接入和运行身份，容量租赁描述可用能力如何被安排使用。"
        },
        {
          "term": "电力现货市场",
          "description": "现货市场按时段交易电能，容量租赁围绕可用功率、电量或服务能力安排。"
        },
        {
          "term": "共享储能",
          "description": "共享储能强调多个主体共享容量或服务，可能通过容量租赁实现。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解租用的是储能能力和服务安排，而不是直接购买一块电池。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注可用功率、电量、SOC 和调用边界。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分项目资产、可用容量和具体市场交易机制。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "独立储能",
        "icon": "battery",
        "href": "/terms/utility-scale-storage/independent-storage/"
      },
      {
        "name": "电力现货市场",
        "icon": "gauge",
        "href": "/terms/utility-scale-storage/spot-market/"
      },
      {
        "name": "共享储能",
        "icon": "battery"
      },
      {
        "name": "AGC／自动发电控制",
        "icon": "gauge",
        "href": "/terms/utility-scale-storage/agc/"
      }
    ],
    "sources": [
      {
        "label": "国家能源局",
        "title": "关于加快推动新型储能发展的指导意见",
        "href": "https://www.nea.gov.cn/139896047_16189891532151n.pdf"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "大型储能"
}
```

<a id="term-solar-charging-ev-charging-infrastructure"></a>
## 充电设施 · 光储充一体化

```json
{
  "id": "term-solar-charging-ev-charging-infrastructure",
  "sourceFile": "src/content/terms/solar-charging-ev-charging-infrastructure.md",
  "sitePath": "/terms/solar-storage-charging/ev-charging-infrastructure/",
  "reviewRecord": {
    "termId": "term-solar-charging-ev-charging-infrastructure",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "光储充正式内容，已确认术语边界、图示关系和参考来源。"
    ]
  },
  "content": {
    "id": "term-solar-charging-ev-charging-infrastructure",
    "contentVersion": 1,
    "scene": "solar-storage-charging",
    "name": "充电设施",
    "english": "EV Charging Infrastructure",
    "termType": "device",
    "category": "设备",
    "summary": "把系统分配的电能提供给园区或充电场站车辆负载的设施。",
    "definition": "充电设施是光储充场站中面向车辆或充电负载执行充电的设备与接口部分。",
    "explanation": {
      "title": "通俗解释",
      "copy": "充电设施就是“把电送到车上的执行端”：它按照允许的功率和场站调度安排完成充电。"
    },
    "boundary": {
      "coreTitle": "系统边界",
      "coreCopy": "本页不描述具体充电接口、额定参数或运营平台功能。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "充电负载",
          "description": "充电负载表示车辆或需求，充电设施是执行供电的设备。"
        },
        {
          "term": "有序充电",
          "description": "有序充电是调度策略，不是充电设施本身。"
        },
        {
          "term": "功率分配",
          "description": "功率分配决定当前给充电设施多少功率，但不代表固定优先级。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "关注车辆什么时候开始充电、充得多快。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注供电边界、设备能力和系统配置。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分充电需求、功率安排和实际执行反馈。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "光伏系统",
        "icon": "home",
        "href": "/terms/solar-storage-charging/pv-system/"
      },
      {
        "name": "储能系统",
        "icon": "battery",
        "href": "/terms/solar-storage-charging/energy-storage-system/"
      },
      {
        "name": "有序充电",
        "icon": "gauge",
        "href": "/terms/solar-storage-charging/managed-charging/"
      }
    ],
    "sources": [
      {
        "label": "U.S. Department of Energy",
        "title": "Electric Vehicle Charging",
        "href": "https://www.energy.gov/energysaver/electric-vehicles"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "光储充一体化"
}
```

<a id="term-solar-charging-ems"></a>
## EMS／能量管理系统 · 光储充一体化

```json
{
  "id": "term-solar-charging-ems",
  "sourceFile": "src/content/terms/solar-charging-ems.md",
  "sitePath": "/terms/solar-storage-charging/ems/",
  "reviewRecord": {
    "termId": "term-solar-charging-ems",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "光储充正式内容，已确认术语边界、图示关系和参考来源。"
    ]
  },
  "content": {
    "id": "term-solar-charging-ems",
    "contentVersion": 1,
    "scene": "solar-storage-charging",
    "name": "EMS／能量管理系统",
    "english": "Energy Management System",
    "termType": "system",
    "category": "系统",
    "summary": "结合光伏发电、储能状态、充电需求和并网点功率安排场站运行的管理系统。",
    "definition": "EMS 根据光伏发电、储能、电网、充电需求和并网点功率信息，在设备允许条件下协调场站运行。",
    "explanation": {
      "title": "通俗解释",
      "copy": "EMS 是光储充场站的“调度大脑”：它看现在有多少电、充电需要多少电，再安排光伏、储能、电网和充电设施怎么配合。"
    },
    "aliases": [
      "EMS"
    ],
    "systemContent": {
      "responsibilities": [
        "EMS 接收发电、储能、充电需求和并网点功率信息并安排运行。",
        "储能系统提供电量缓冲，充电设施执行充电。",
        "实际执行仍受设备能力和系统允许条件约束。"
      ],
      "dataDimensions": [
        {
          "name": "光伏发电与电网供电",
          "description": "反映当前可用的供电来源。"
        },
        {
          "name": "储能状态",
          "description": "反映 SOC 和当前充放电允许范围。"
        },
        {
          "name": "充电需求",
          "description": "反映园区或场站的车辆充电负载需要多少功率。"
        }
      ],
      "scenarios": [
        {
          "name": "有序充电",
          "description": "EMS 根据需求和可用功率安排充电时段与功率。"
        },
        {
          "name": "功率分配",
          "description": "EMS 在光伏、储能、电网和充电之间协调当前分配。"
        }
      ],
      "topologyBindings": [
        {
          "sceneId": "scene-solar-storage-charging",
          "topologyId": "solar-ems-relations",
          "isPrimary": true,
          "verificationStatus": "unverified",
          "evidenceRefs": [
            "phase-four-preview"
          ]
        }
      ]
    },
    "boundary": {
      "coreTitle": "系统边界",
      "coreCopy": "本页只表达调度关系，不假定 EMS 是独立硬件、云端服务或固定通信方式。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "充电设施",
          "description": "充电设施执行充电，EMS 负责安排运行。"
        },
        {
          "term": "储能系统",
          "description": "储能系统提供缓冲能力，但不替代 EMS 的调度职责。"
        },
        {
          "term": "功率分配",
          "description": "功率分配是 EMS 可能执行的目标之一，不是 EMS 的全部定义。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解为什么充电功率会随光照、储能和系统安排变化。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注发电、储能、电网和充电设备的允许条件。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分充电需求、调度安排和实际功率反馈。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "光伏系统",
        "icon": "home",
        "href": "/terms/solar-storage-charging/pv-system/"
      },
      {
        "name": "储能系统",
        "icon": "battery",
        "href": "/terms/solar-storage-charging/energy-storage-system/"
      },
      {
        "name": "有序充电",
        "icon": "gauge",
        "href": "/terms/solar-storage-charging/managed-charging/"
      },
      {
        "name": "功率分配",
        "icon": "gauge",
        "href": "/terms/solar-storage-charging/power-allocation/"
      }
    ],
    "sources": [
      {
        "label": "U.S. Department of Energy",
        "title": "Energy Storage",
        "href": "https://www.energy.gov/oe/energy-storage"
      },
      {
        "label": "U.S. Department of Energy",
        "title": "Electric Vehicle Charging",
        "href": "https://www.energy.gov/energysaver/electric-vehicles"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "光储充一体化"
}
```

<a id="term-solar-charging-energy-storage-system"></a>
## 储能系统 · 光储充一体化

```json
{
  "id": "term-solar-charging-energy-storage-system",
  "sourceFile": "src/content/terms/solar-charging-energy-storage-system.md",
  "sitePath": "/terms/solar-storage-charging/energy-storage-system/",
  "reviewRecord": {
    "termId": "term-solar-charging-energy-storage-system",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "光储充正式内容，已确认术语边界、图示关系和参考来源。"
    ]
  },
  "content": {
    "id": "term-solar-charging-energy-storage-system",
    "contentVersion": 1,
    "scene": "solar-storage-charging",
    "name": "储能系统",
    "english": "Energy Storage System",
    "termType": "system",
    "category": "系统",
    "summary": "在园区或充电场站暂存和释放电能，用于缓冲发电与充电需求变化的系统。",
    "definition": "储能系统在允许条件下吸收、保存并释放电能，帮助协调光伏发电、电网供电和场站充电需求。",
    "explanation": {
      "title": "通俗解释",
      "copy": "储能系统像光储充场站里的“电量缓冲区”：光伏多发时先存下来，充电需求高时再按条件补一部分电。"
    },
    "systemContent": {
      "responsibilities": [
        "储能系统在允许条件下吸收或释放电能。",
        "EMS 根据发电、充电需求和状态安排运行。",
        "PCS、BMS 等部分共同决定执行边界。"
      ],
      "dataDimensions": [
        {
          "name": "SOC",
          "description": "表示当前荷电状态，影响还能存多少或放多少。"
        },
        {
          "name": "充电需求",
          "description": "反映园区或场站车辆充电负载的当前需求。"
        },
        {
          "name": "可用功率",
          "description": "反映当前能够安排的充放电功率范围。"
        }
      ],
      "scenarios": [
        {
          "name": "光伏过剩缓冲",
          "description": "发电多于即时需求时，系统可能安排充电。"
        },
        {
          "name": "充电支持",
          "description": "充电需求较高时，系统可能在允许条件下释放电能。"
        }
      ],
      "topologyBindings": [
        {
          "sceneId": "scene-solar-storage-charging",
          "topologyId": "solar-energy-storage-system-relations",
          "isPrimary": true,
          "verificationStatus": "unverified",
          "evidenceRefs": [
            "phase-four-preview"
          ]
        }
      ]
    },
    "boundary": {
      "coreTitle": "系统边界",
      "coreCopy": "本页不绑定某种储能电池、PCS 或充电设备配置。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "光伏系统",
          "description": "光伏系统负责发电，储能系统负责存储和释放。"
        },
        {
          "term": "充电设施",
          "description": "储能系统提供电能缓冲，充电设施负责面向车辆或负载执行充电。"
        },
        {
          "term": "功率分配",
          "description": "储能是否优先充电或放电以系统策略和允许条件为准。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解储能为什么会在不同时间充电或放电。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注电池状态、功率边界和供需关系。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分系统可用电量、功率能力和当前调度动作。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "光伏系统",
        "icon": "home",
        "href": "/terms/solar-storage-charging/pv-system/"
      },
      {
        "name": "充电设施",
        "icon": "chip",
        "href": "/terms/solar-storage-charging/ev-charging-infrastructure/"
      },
      {
        "name": "有序充电",
        "icon": "gauge",
        "href": "/terms/solar-storage-charging/managed-charging/"
      }
    ],
    "sources": [
      {
        "label": "U.S. Department of Energy",
        "title": "Energy Storage",
        "href": "https://www.energy.gov/oe/energy-storage"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "光储充一体化"
}
```

<a id="term-solar-charging-pv-system"></a>
## 光伏系统 · 光储充一体化

```json
{
  "id": "term-solar-charging-pv-system",
  "sourceFile": "src/content/terms/solar-charging-pv-system.md",
  "sitePath": "/terms/solar-storage-charging/pv-system/",
  "reviewRecord": {
    "termId": "term-solar-charging-pv-system",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "光储充正式内容，已确认术语边界、图示关系和参考来源。"
    ]
  },
  "content": {
    "id": "term-solar-charging-pv-system",
    "contentVersion": 1,
    "scene": "solar-storage-charging",
    "name": "光伏系统",
    "english": "Photovoltaic System",
    "termType": "system",
    "category": "系统",
    "summary": "把太阳能转换为电能，并为园区或充电场站的储能和充电负载提供发电来源的系统。",
    "definition": "光伏系统通过光伏组件及相关设备将太阳能转换为电能，发电量会随光照和场站条件变化。",
    "explanation": {
      "title": "通俗解释",
      "copy": "光伏系统就是光储充场站里的“发电来源”：有光时先产生电，再由系统安排直接供给充电、存入储能或补充其他需求。"
    },
    "aliases": [
      "PV System"
    ],
    "systemContent": {
      "responsibilities": [
        "光伏系统提供随光照变化的发电量。",
        "EMS 结合发电、储能状态和充电需求安排运行。",
        "储能和充电设施在允许条件内执行。"
      ],
      "dataDimensions": [
        {
          "name": "光伏发电量",
          "description": "反映当前或一段时间内的发电情况。"
        },
        {
          "name": "可用功率",
          "description": "反映当前可以分配给储能或充电负载的功率。"
        },
        {
          "name": "发电状态",
          "description": "反映光伏系统当前是否有足够发电可供使用。"
        }
      ],
      "scenarios": [
        {
          "name": "直接供电",
          "description": "发电条件满足时，电能可以被充电负载直接使用。"
        },
        {
          "name": "储能缓冲",
          "description": "暂时多出的电能可以在允许条件下存入储能系统。"
        }
      ],
      "topologyBindings": [
        {
          "sceneId": "scene-solar-storage-charging",
          "topologyId": "solar-pv-system-relations",
          "isPrimary": true,
          "verificationStatus": "unverified",
          "evidenceRefs": [
            "phase-four-preview"
          ]
        }
      ]
    },
    "boundary": {
      "coreTitle": "系统边界",
      "coreCopy": "本页只解释光伏在园区或充电场站中的发电角色，不展开组件选型和工程接线。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "储能系统",
          "description": "光伏系统负责发电，储能系统负责存储和释放电能。"
        },
        {
          "term": "充电设施",
          "description": "充电设施负责执行充电，光伏系统不等于充电设备。"
        },
        {
          "term": "功率分配",
          "description": "EMS 负责协调可用电能与需求，不代表固定优先级。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "理解充电电能可能来自光伏、储能或电网。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注发电波动、转换边界和系统配置。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分发电数据、可用功率和充电执行状态。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "储能系统",
        "icon": "battery",
        "href": "/terms/solar-storage-charging/energy-storage-system/"
      },
      {
        "name": "EMS／能量管理系统",
        "icon": "chip",
        "href": "/terms/solar-storage-charging/ems/"
      },
      {
        "name": "功率分配",
        "icon": "gauge",
        "href": "/terms/solar-storage-charging/power-allocation/"
      }
    ],
    "sources": [
      {
        "label": "U.S. Department of Energy",
        "title": "Solar Energy",
        "href": "https://www.energy.gov/energysaver/solar-energy"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "光储充一体化"
}
```

<a id="term-utility-independent-storage"></a>
## 独立储能 · 大型储能

```json
{
  "id": "term-utility-independent-storage",
  "sourceFile": "src/content/terms/utility-independent-storage.md",
  "sitePath": "/terms/utility-scale-storage/independent-storage/",
  "reviewRecord": {
    "termId": "term-utility-independent-storage",
    "contentVersion": 1,
    "status": "reviewed",
    "contentReviewed": true,
    "boundaryReviewed": true,
    "sourcesReviewed": true,
    "reviewedBy": "产品确认",
    "reviewNotes": [
      "已确认独立储能作为大型储能正式场景的默认主模型。"
    ]
  },
  "content": {
    "id": "term-utility-independent-storage",
    "contentVersion": 1,
    "scene": "utility-scale-storage",
    "name": "独立储能",
    "english": "Independent Energy Storage",
    "termType": "system",
    "category": "项目形态",
    "summary": "直接接入公共电网、独立接受调度并提供电力服务的储能项目形态。",
    "definition": "独立储能是与发电侧或用电侧主体相对独立、通过并网连接点接入公共电网，并按调度或市场要求运行的储能项目形态。",
    "explanation": {
      "title": "通俗解释",
      "copy": "独立储能可以理解成单独建在电网侧的“大型电量仓库”：它不服务某一家工厂，而是根据电网和市场需要充电、放电或提供响应。"
    },
    "systemContent": {
      "responsibilities": [
        "独立储能通过并网连接点与公共电网交换电能。",
        "EMS、PCS、BMS 和电池系统共同完成调度、转换与状态保护。",
        "电站可以按适用规则提供能量、容量或辅助服务。"
      ],
      "dataDimensions": [
        {
          "name": "并网点功率",
          "description": "反映储能电站与公共电网之间的功率交换。"
        },
        {
          "name": "可用容量与电量",
          "description": "反映当前可以承诺或执行的功率和电量范围。"
        },
        {
          "name": "调度与市场要求",
          "description": "反映电站当前需要跟随的运行、服务或交易安排。"
        }
      ],
      "scenarios": [
        {
          "name": "并网运行",
          "description": "电站通过 POC 与公共电网保持连接，并按允许条件交换电能。"
        },
        {
          "name": "辅助服务",
          "description": "电站在能力和规则允许时响应 AGC、调频或备用等要求。"
        }
      ],
      "topologyBindings": [
        {
          "sceneId": "scene-utility-scale-storage",
          "topologyId": "utility-scale-storage-relations",
          "isPrimary": true,
          "verificationStatus": "unverified",
          "evidenceRefs": [
            "phase-four-scope"
          ]
        }
      ]
    },
    "boundary": {
      "coreTitle": "项目边界",
      "coreCopy": "独立储能描述项目的接入和运行身份，不等于某一种设备、某一项辅助服务或固定收益模式。",
      "rowsTitle": "容易混淆",
      "rows": [
        {
          "term": "共享储能",
          "description": "共享储能描述容量和服务如何被多个主体使用，项目也可能采用独立储能的接入形态。"
        },
        {
          "term": "工商业储能",
          "description": "工商业储能通常围绕用户侧负荷和用电目标，独立储能主要面向公共电网侧运行。"
        },
        {
          "term": "电池储能系统／BESS",
          "description": "BESS 关注系统组成，独立储能关注项目如何接入和服务电网。"
        }
      ]
    },
    "roles": [
      {
        "name": "使用侧",
        "description": "看懂大型储能为什么单独建站，以及它服务的对象是谁。",
        "icon": "user"
      },
      {
        "name": "工程侧",
        "description": "关注 POC、站内设备、并网条件和可用功率之间的关系。",
        "icon": "wrench"
      },
      {
        "name": "产品侧",
        "description": "区分项目形态、设备组成、调度服务和市场机制。",
        "icon": "cube"
      }
    ],
    "relatedTerms": [
      {
        "name": "POC／并网连接点",
        "icon": "chip",
        "href": "/terms/utility-scale-storage/poc/"
      },
      {
        "name": "AGC／自动发电控制",
        "icon": "gauge",
        "href": "/terms/utility-scale-storage/agc/"
      },
      {
        "name": "容量租赁",
        "icon": "battery",
        "href": "/terms/utility-scale-storage/capacity-lease/"
      },
      {
        "name": "电力现货市场",
        "icon": "gauge",
        "href": "/terms/utility-scale-storage/spot-market/"
      }
    ],
    "sources": [
      {
        "label": "国家能源局",
        "title": "关于加快推动新型储能发展的指导意见",
        "href": "https://www.nea.gov.cn/139896047_16189891532151n.pdf"
      }
    ],
    "publicationStatus": "published"
  },
  "sceneLabel": "大型储能"
}
```
