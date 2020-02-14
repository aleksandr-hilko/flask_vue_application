<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-10">
        <br />
        <br />
        <button type="button" class="btn btn-success btn-sm">Добавить Объект</button>
        <br />
        <br />
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Название</th>
              <th scope="col">Заказчик</th>
              <th scope="col">Договор</th>
              <th scope="col">Цена</th>
              <th scope="col">Съёмка</th>
              <th scope="col">Начало работ</th>
              <th scope="col">Окончание работ</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <project
                v-for="(project, item) in projects"
                :key="item"
                :data="project"
                @deleteProject="handleDeleteProject($event)">
            </project>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Project from '@/components/Project';

export default {
  name: 'ProjectList',
  components: {
    Project,
  },
  data() {
    return {
      projects: [],
    };
  },
  methods: {
    getProjects() {
      const path = 'http://localhost:5000/api/projects';
      axios
        .get(path)
        .then((res) => {
          this.projects = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    handleDeleteProject() {
      this.getProjects();
    },
  },
  created() {
    this.getProjects();
  },
};
</script>

<style>
    .container-fluid {
        margin-left: 10%;
    }
</style>
