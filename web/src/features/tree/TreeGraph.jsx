import { useMemo, useRef, useState } from "react";
import { Button, Empty, Space, Tag } from "antd";
import { ExpandOutlined, MinusOutlined, PlusOutlined } from "@ant-design/icons";
import { graphLayout } from "./model.js";

export default function TreeGraph({ rows, selected, onSelect }) {
  const layout = useMemo(() => graphLayout(rows), [rows]);
  const [zoom, setZoom] = useState(1);
  const viewport = useRef(null);
  const drag = useRef(null);
  const positions = [...layout.positions.entries()];
  const fit = () => {
    const bounds = viewport.current;
    setZoom(
      Math.min(
        1,
        Math.max(
          0.025,
          Math.min(
            bounds.clientWidth / layout.width,
            bounds.clientHeight / layout.height,
          ),
        ),
      ),
    );
    bounds.scrollTo(0, 0);
  };
  return (
    <div className="graph-region">
      <div
        className="graph-viewport"
        ref={viewport}
        onPointerDown={(event) => {
          if (event.button !== 0 || event.target.closest("button")) return;
          drag.current = {
            x: event.clientX,
            y: event.clientY,
            left: viewport.current.scrollLeft,
            top: viewport.current.scrollTop,
          };
          event.currentTarget.setPointerCapture(event.pointerId);
        }}
        onPointerMove={(event) => {
          if (drag.current)
            viewport.current.scrollTo(
              drag.current.left + drag.current.x - event.clientX,
              drag.current.top + drag.current.y - event.clientY,
            );
        }}
        onPointerUp={() => {
          drag.current = null;
        }}
        onPointerCancel={() => {
          drag.current = null;
        }}
      >
        {!rows.length ? (
          <Empty description="没有匹配的节点" />
        ) : (
          <div
            className="graph-scaled"
            style={{ width: layout.width * zoom, height: layout.height * zoom }}
          >
            <div
              className="graph-canvas"
              style={{
                width: layout.width,
                height: layout.height,
                transform: `scale(${zoom})`,
              }}
            >
              <svg
                width={layout.width}
                height={layout.height}
                aria-hidden="true"
              >
                <g fill="none" stroke="#b4c9e1" strokeWidth="1.5">
                  {positions.map(([id, p]) => {
                    const parent = layout.positions.get(p.row.node.parent);
                    return parent ? (
                      <path
                        key={id}
                        d={`M${parent.x + 246},${parent.y + 31} C${parent.x + 269},${parent.y + 31} ${p.x - 23},${p.y + 31} ${p.x},${p.y + 31}`}
                      />
                    ) : null;
                  })}
                </g>
              </svg>
              {positions.map(([id, p]) => (
                <Button
                  key={id}
                  className={`graph-node ${selected === id ? "selected" : ""}`}
                  style={{ left: p.x, top: p.y }}
                  onClick={() => onSelect(id)}
                >
                  <span className="graph-title">
                    <strong>{p.row.node.name.zh}</strong>
                    <Tag color="blue">{p.row.node.level}</Tag>
                  </span>
                  <span className="graph-node-id">{id}</span>
                </Button>
              ))}
            </div>
          </div>
        )}
      </div>
      <div className="graph-tools">
        <Space.Compact>
          <Button
            icon={<MinusOutlined />}
            aria-label="缩小"
            onClick={() => setZoom((current) => Math.max(0.025, current / 1.2))}
          />
          <Button onClick={() => setZoom(1)}>{Math.round(zoom * 100)}%</Button>
          <Button
            icon={<PlusOutlined />}
            aria-label="放大"
            onClick={() => setZoom((current) => Math.min(2, current * 1.2))}
          />
        </Space.Compact>
        <Button icon={<ExpandOutlined />} onClick={fit}>
          适应画布
        </Button>
      </div>
      <div className="graph-instruction">拖动画布平移，点击节点查看详情</div>
    </div>
  );
}
