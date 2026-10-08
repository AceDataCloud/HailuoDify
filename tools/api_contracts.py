"""Published API contracts; source revisions are recorded in tests/parity-audit.json."""

TASK_PATH = "/hailuo/tasks"

ENDPOINTS = {
    "hailuo_generate_video": {
        "method": "POST",
        "path": "/hailuo/videos",
        "operation": "generate",
        "schema": {
            "type": "object",
            "required": ["action"],
            "properties": {
                "model": {
                    "enum": ["minimax-i2v", "minimax-t2v", "minimax-i2v-director"],
                    "type": "string",
                },
                "action": {"enum": ["generate"], "type": "string"},
                "prompt": {"type": "string"},
                "callback_url": {"type": "string"},
                "async": {"type": "boolean"},
                "first_image_url": {"type": "string"},
            },
        },
        "properties": {
            "model": {
                "enum": ["minimax-i2v", "minimax-t2v", "minimax-i2v-director"],
                "type": "string",
            },
            "action": {"enum": ["generate"], "type": "string"},
            "prompt": {"type": "string"},
            "callback_url": {"type": "string"},
            "async": {"type": "boolean"},
            "first_image_url": {"type": "string"},
        },
        "parameters": [],
        "defaults": {"model": "minimax-t2v", "action": "generate"},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
        "media_response": False,
    },
    "hailuo_task_retrieve": {
        "method": "POST",
        "path": "/hailuo/tasks",
        "operation": "task",
        "schema": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "ids": {"type": "array", "items": {"type": "string"}},
                "action": {"enum": ["retrieve", "retrieve_batch"], "type": "string"},
            },
        },
        "properties": {
            "id": {"type": "string"},
            "ids": {"type": "array", "items": {"type": "string"}},
            "action": {"enum": ["retrieve", "retrieve_batch"], "type": "string"},
        },
        "parameters": [],
        "defaults": {"wait_seconds": 0},
        "fixed": {},
        "allow_empty": [],
        "query_actions": ["retrieve", "retrieve_batch", "list", "presets"],
        "media_response": False,
    },
    "hailuo_tasks_retrieve_batch": {
        "method": "POST",
        "path": "/hailuo/tasks",
        "operation": "batch",
        "schema": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "ids": {"type": "array", "items": {"type": "string"}, "minItems": 1},
                "action": {"enum": ["retrieve", "retrieve_batch"], "type": "string"},
            },
            "required": ["action", "ids"],
        },
        "properties": {
            "id": {"type": "string"},
            "ids": {"type": "array", "items": {"type": "string"}, "minItems": 1},
            "action": {"enum": ["retrieve", "retrieve_batch"], "type": "string"},
        },
        "parameters": [],
        "defaults": {},
        "fixed": {"action": "retrieve_batch"},
        "allow_empty": [],
        "query_actions": ["retrieve", "retrieve_batch", "list", "presets"],
        "media_response": False,
    },
}
