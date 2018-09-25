CREATE OR REPLACE VIEW "public" ."wlm_queue_state_vw"
AS
SELECT config.service_class - 5 AS queue,
       BTRIM("class".condition::CHARACTER VARYING::TEXT) AS description,
       config.num_query_tasks AS slots,
       config.query_working_mem AS mem,
       config.max_execution_time AS max_time,
       config.user_group_wild_card AS "user_*",
       config.query_group_wild_card AS "query_*",
       state.num_queued_queries AS queued,
       state.num_executing_queries AS executing,
       state.num_executed_queries AS executed
FROM stv_wlm_classification_config "class",
     stv_wlm_service_class_config config,
     stv_wlm_service_class_state state
WHERE "class".action_service_class = config.service_class
AND   "class".action_service_class = state.service_class
AND   config.service_class > 4
ORDER BY config.service_class



