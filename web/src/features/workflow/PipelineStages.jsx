import { Typography } from "antd";
import { pipelineLayers } from "./pipeline.js";
import "./pipeline.css";

const names = {
  "ft-android": "Android 事实研究", "ft-ios": "iOS 事实研究", "ft-harmonyos": "HarmonyOS 事实研究",
  "ft-align": "三端能力对齐", "ft-design": "特性树设计", "ft-bind": "API 与叶子绑定",
  "ft-check": "确定性校验", "ft-granularity": "粒度审查", "ft-coverage": "覆盖审查", "ft-review": "独立审查", "ft-integrate": "跨领域整合",
  "fk-scope": "叶子研究范围", "fk-android": "Android 知识研究", "fk-ios": "iOS 知识研究", "fk-harmonyos": "HarmonyOS 知识研究",
  "fk-compare": "三端差异比较", "fk-review": "独立审查", "fk-confidence": "逐结论可信度", "fk-assemble": "知识组装",
};
export default function PipelineStages({ plan, tasks, renderTask }) {
  return <section aria-label="按执行顺序排列的流水线" className="workflow-pipeline">
    <Typography.Paragraph type="secondary">从上到下按依赖推进；同一层的 Agent 可并行执行。后续阶段等待所需上游产物通过校验。</Typography.Paragraph>
    {pipelineLayers(plan).map((ids, index) => <section className="pipeline-layer" key={ids.join(",")} aria-label={`第 ${index + 1} 阶段`}>
      <div className="pipeline-number" aria-hidden="true">{index + 1}</div>
      <div className="pipeline-content">
        <Typography.Title level={5}>第 {index + 1} 阶段 · {ids.length > 1 ? "并行执行" : names[ids[0]] || ids[0]}</Typography.Title>
        <div className="pipeline-cards">{ids.map(id => <div className="pipeline-lane" key={id}>
          <Typography.Text strong>{names[id] || id}</Typography.Text>
          {plan.works.flatMap(work => tasks.filter(task => task.stage_id === id && task.work_id === work.id)).map(task => renderTask(task))}
        </div>)}</div>
      </div>
    </section>)}
  </section>;
}
