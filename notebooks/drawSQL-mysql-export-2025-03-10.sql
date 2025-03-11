CREATE TABLE `record`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `record_number` BIGINT NOT NULL,
    `property` BIGINT NOT NULL,
    `status` BIGINT NOT NULL,
    `issue_date` DATETIME NOT NULL,
    `number_of_units` FLOAT(53) NOT NULL,
    `current_property_use` BIGINT NOT NULL,
    `building_use` BIGINT NOT NULL,
    `costs` BIGINT NOT NULL,
    `total_cost_bins` BIGINT NOT NULL,
    `description` VARCHAR(255) NOT NULL,
    `isd_description` VARCHAR(255) NOT NULL,
    `size_of_new_addition` FLOAT(53) NOT NULL,
    `change_in_floor_area_or_dimensions` BOOLEAN NOT NULL,
    `change_in_exterior` BOOLEAN NOT NULL,
    `discharge_to_sewer_or_storm_water_system` BOOLEAN NOT NULL,
    `new_or_replaced_storm_sewer` BOOLEAN NOT NULL,
    `construction_dewatering` BOOLEAN NOT NULL,
    `public_right-of-way` BOOLEAN NOT NULL,
    `basement_plumbing_fixture` BOOLEAN NOT NULL,
    `change_in_at_least_half_of_total_area` BOOLEAN NOT NULL,
    `firm_name` BIGINT NOT NULL,
    `debris_disposal` VARCHAR(255) NOT NULL,
    `description_of_demolition` VARCHAR(255) NOT NULL,
    `method_of_removal` VARCHAR(255) NOT NULL,
    `type_of_demolition` VARCHAR(255) NOT NULL,
    `condo_association` BOOLEAN NOT NULL,
    `building_construction_type` BIGINT NOT NULL,
    `bza_case` BOOLEAN NOT NULL,
    `planning_board_special_permit` BOOLEAN NOT NULL,
    `bicycle_parking_change` BOOLEAN NOT NULL,
    `issue_year` INT NOT NULL,
    `issue_month` INT NOT NULL,
    `season` BIGINT NOT NULL,
    `keywords` BIGINT NOT NULL
);
CREATE TABLE `status`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `value` BIGINT NOT NULL
);
CREATE TABLE `building_use`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `use` BIGINT NOT NULL
);
CREATE TABLE `property`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `address` VARCHAR(255) NOT NULL,
    `latitude` FLOAT(53) NOT NULL,
    `longitude` FLOAT(53) NOT NULL
);
CREATE TABLE `costs`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `building_cost` FLOAT(53) NOT NULL,
    `electrical_cost` FLOAT(53) NOT NULL,
    `plumbing_cost` FLOAT(53) NOT NULL,
    `gas_cost` FLOAT(53) NOT NULL,
    `hvac_cost` FLOAT(53) NOT NULL,
    `fire_prevention_cost` FLOAT(53) NOT NULL,
    `calc_total_cost` FLOAT(53) NOT NULL
);
CREATE TABLE `firm`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `firm_name` VARCHAR(255) NOT NULL,
    `standardized_firm_name` VARCHAR(255) NOT NULL
);
CREATE TABLE `building_construction_type`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `type` BIGINT NOT NULL
);
CREATE TABLE `season`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` BIGINT NOT NULL
);
CREATE TABLE `total_cost_bins`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `bin_name` VARCHAR(255) NOT NULL
);
CREATE TABLE `record_keyword`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `record_id` BIGINT NOT NULL,
    `keyword_id` BIGINT NOT NULL
);
CREATE TABLE `keyword`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `keyword` VARCHAR(255) NOT NULL
);
-- ALTER TABLE
--     `record` ADD CONSTRAINT `record_total_cost_bins_foreign` FOREIGN KEY(`total_cost_bins`) REFERENCES `total_cost_bins`(`id`);
-- ALTER TABLE
--     `record` ADD CONSTRAINT `record_costs_foreign` FOREIGN KEY(`costs`) REFERENCES `costs`(`id`);
-- ALTER TABLE
--     `record` ADD CONSTRAINT `record_property_foreign` FOREIGN KEY(`property`) REFERENCES `property`(`address`);
-- ALTER TABLE
--     `record_keyword` ADD CONSTRAINT `record_keyword_keyword_id_foreign` FOREIGN KEY(`keyword_id`) REFERENCES `keyword`(`id`);
-- ALTER TABLE
--     `record` ADD CONSTRAINT `record_firm_name_foreign` FOREIGN KEY(`firm_name`) REFERENCES `firm`(`id`);
-- ALTER TABLE
--     `record` ADD CONSTRAINT `record_status_foreign` FOREIGN KEY(`status`) REFERENCES `status`(`id`);
-- ALTER TABLE
--     `record` ADD CONSTRAINT `record_season_foreign` FOREIGN KEY(`season`) REFERENCES `season`(`id`);
-- ALTER TABLE
--     `record` ADD CONSTRAINT `record_building_construction_type_foreign` FOREIGN KEY(`building_construction_type`) REFERENCES `building_construction_type`(`id`);
-- ALTER TABLE
--     `record` ADD CONSTRAINT `record_building_use_foreign` FOREIGN KEY(`building_use`) REFERENCES `building_use`(`id`);
-- ALTER TABLE
--     `record` ADD CONSTRAINT `record_current_property_use_foreign` FOREIGN KEY(`current_property_use`) REFERENCES `building_use`(`id`);
-- ALTER TABLE
--     `record` ADD CONSTRAINT `record_keywords_foreign` FOREIGN KEY(`keywords`) REFERENCES `record_keyword`(`record_id`);