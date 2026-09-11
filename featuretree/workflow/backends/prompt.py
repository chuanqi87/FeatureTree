"""Small launch instructions; full stage inputs remain available in the workspace."""


def execution_prompt(packet, workspace):
    prompt = (
        "读取当前目录 task.json，执行其中的工作单。使用常规 read/write/edit/bash/grep/glob 等工具，"
        "可以编写脚本、分步保存和编辑工作文件，自行安排研究和实现步骤。"
        "source_catalog 可查询封存来源；submit_payload/finish_payload 是可选辅助工具。"
        "将符合 task.json 中 output_schema 的完整 JSON 信封写入 delivery/result.json。"
        "固定身份字段从 task.json 复制，reviewed_hash 使用工作单给定值（如有）。"
        "完成后检查 JSON 和必填内容，再退出；最终聊天无需复述正文。"
        "日志中的 length 仅记录单次输出耗尽，最终按退出状态、交付文件及完整业务校验验收。"
        "保留原有证据要求、输入完整性和独立审查职责。\n"
    )
    if packet.get("batch"):
        prompt += "此工作单显式启用了分批，仅完成本批输入，其他批次由执行器汇总。\n"
    if packet.get("response_repair"):
        prompt += "本次仅修复 response_repair 中保留的 JSON 格式，不重新研究或修改结论。\n"
    return (f"本次工作区绝对路径：{workspace}。\n工作单：{workspace / 'task.json'}。\n"
            f"最终交付：{workspace / 'delivery/result.json'}。\n"
            "原生工具可能默认使用 Git 根目录，请使用上述绝对路径，bash 显式指定本次工作区 workdir。\n"
            + prompt)
